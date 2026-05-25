import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io
import smtplib
import json
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# ==========================================
# ⚙️ CONFIGURAÇÕES DE E-MAIL
# ==========================================
EMAIL_REMETENTE = "vesda.ai.analytics@gmail.com"
SENHA_DO_EMAIL = "dugn fhbu nrzy xweo"
EMAIL_PADRAO_CONSULTOR = "silviosileiravasconcelos@hotmail.com"

FICHEIRO_CONFIG = "config_veda.json"

def carregar_email_consultor():
    if os.path.exists(FICHEIRO_CONFIG):
        try:
            with open(FICHEIRO_CONFIG, 'r') as f:
                dados = json.load(f)
                return dados.get("email_consultor", EMAIL_PADRAO_CONSULTOR)
        except:
            return EMAIL_PADRAO_CONSULTOR
    return EMAIL_PADRAO_CONSULTOR

def guardar_email_consultor(novo_email):
    with open(FICHEIRO_CONFIG, 'w') as f:
        json.dump({"email_consultor": novo_email}, f)

EMAIL_CONSULTOR_ATUAL = carregar_email_consultor()

# Configuração da página
st.set_page_config(page_title="VEDA.IA - Diagnóstico Estratégico", layout="wide", initial_sidebar_state="collapsed")

# --- Interface de Design Premium (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #1E293B !important; color: #F8FAFC !important; font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .stMarkdown, p, span, label, .stTextArea label { color: #F8FAFC !important; }
    .main-header { background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 100%); padding: 20px; border-radius: 12px; color: white !important; margin-bottom: 25px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.2); border: 1px solid #334155; }
    .main-title { font-size: 32px; font-weight: 800; letter-spacing: -0.5px; margin: 0; color: #FFFFFF !important; }
    .subtitle { font-size: 15px; color: #93C5FD !important; margin-top: 5px; opacity: 0.9; }
    .section-box { background-color: #334155 !important; padding: 24px; border-radius: 10px; border-left: 6px solid #38BDF8; margin-bottom: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .section-title { font-size: 18px; font-weight: 700; color: #38BDF8 !important; margin: 0; }
    .stTextArea textarea { background-color: #1E293B !important; color: #FFFFFF !important; border: 1px solid #475569 !important; border-radius: 6px !important; }
    </style>
""", unsafe_allow_html=True)

# Inicialização de Variáveis
if 'perfil' not in st.session_state: st.session_state.perfil = 'cliente'
if 'passo' not in st.session_state: st.session_state.passo = 1
if 'respostas' not in st.session_state: st.session_state.respostas = {}

# --- MENU LATERAL (ÁREA DO CONSULTOR) ---
with st.sidebar:
    if st.session_state.perfil == 'cliente':
        senha = st.text_input("Senha Admin", type="password")
        if st.button("Entrar como Consultor", use_container_width=True):
            if senha == "vedaadmin":
                st.session_state.perfil = 'consultor'; st.rerun()
            else: st.error("Senha incorreta.")
    else:
        st.markdown("<h3 style='color:#10B981;'>👨‍💼 Painel do Consultor</h3>", unsafe_allow_html=True)
        novo_email = st.text_input("E-mail para receber relatórios", value=EMAIL_CONSULTOR_ATUAL)
        if st.button("💾 Salvar E-mail", use_container_width=True):
            guardar_email_consultor(novo_email); st.success("E-mail atualizado!")
        if st.button("Sair (Modo Cliente)", use_container_width=True):
            st.session_state.perfil = 'cliente'; st.session_state.passo = 1; st.rerun()

# --- TOPO ---
st.markdown("<div class='main-header'><div class='main-title'>📊 VEDA.IA</div><div class='subtitle'>Inteligência Estratégica em Compras</div></div>", unsafe_allow_html=True)

# --- FUNÇÕES AUXILIARES (PDF/EMAIL) ---
def gerar_ishikawa_pdf():
    fig, ax = plt.subplots(figsize=(10, 3.5)); fig.patch.set_facecolor('#FFFFFF'); ax.set_facecolor('#FFFFFF'); ax.axhline(0, color='#1B365D', linewidth=4)
    ax.annotate('MÉTODO:\nFollow-up manual', xy=(2.5, 0), xytext=(1.0, 1.2), arrowprops=dict(arrowstyle="->", color='#4A777A', lw=2), fontsize=9, color='black')
    ax.annotate('SISTEMAS:\nRedigitação manual', xy=(6.5, 0), xytext=(5.0, 1.2), arrowprops=dict(arrowstyle="->", color='#4A777A', lw=2), fontsize=9, color='black')
    ax.text(10.2, 0, "PERDA DE\nSAVING", fontsize=10, fontweight='bold', color='white', bbox=dict(boxstyle="square,pad=0.5", fc="#A93226", ec="none"))
    ax.axis('off'); img_buffer = io.BytesIO(); fig.savefig(img_buffer, format='png', bbox_inches='tight', dpi=150); img_buffer.seek(0); plt.close(fig); return img_buffer

def gerar_pdf(dados_tabela, ishikawa_buffer):
    buffer = io.BytesIO(); doc = SimpleDocTemplate(buffer, pagesize=letter); story = []
    story.append(Paragraph("RELATÓRIO EXECUTIVO - VEDA.IA", getSampleStyleSheet()['Heading1']))
    story.append(RLImage(ishikawa_buffer, width=400, height=140)); story.append(Spacer(1, 20))
    story.append(Paragraph("PLANO DE AÇÃO", getSampleStyleSheet()['Heading2']))
    # Tabela simplificada
    doc.build(story); buffer.seek(0); return buffer

def enviar_email(respostas, pdf_buffer):
    msg = MIMEMultipart(); msg['From'] = EMAIL_REMETENTE; msg['To'] = carregar_email_consultor(); msg['Subject'] = "🚨 Novo Diagnóstico VEDA.IA"
    msg.attach(MIMEText(str(respostas), 'plain')); anexo = MIMEApplication(pdf_buffer.read(), _subtype="pdf"); anexo.add_header('Content-Disposition', 'attachment', filename="Relatorio.pdf"); msg.attach(anexo)
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587); s.starttls(); s.login(EMAIL_REMETENTE, SENHA_DO_EMAIL); s.send_message(msg); s.quit(); return True
    except: return False

# --- FLUXO DE PERGUNTAS ---
if st.session_state.passo <= 5:
    st.progress(st.session_state.passo / 5)
    
    if st.session_state.passo == 1:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO A: VISÃO ESTRATÉGICA</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['Vol. Requisições'] = st.text_area("1. Volume médio mensal de requisições?")
        if st.button("Avançar"): st.session_state.passo = 2; st.rerun()
    elif st.session_state.passo == 2:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO B: ROTINA</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['Rotina'] = st.text_area("1. Como é a sua rotina?")
        if st.button("Avançar"): st.session_state.passo = 3; st.rerun()
    elif st.session_state.passo == 3:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO C: CADASTROS</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['Cadastros'] = st.text_area("1. Como são os cadastros?")
        if st.button("Avançar"): st.session_state.passo = 4; st.rerun()
    elif st.session_state.passo == 4:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO D: MANUTENÇÃO</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['MRO'] = st.text_area("1. Como é o fluxo de MRO?")
        if st.button("Avançar"): st.session_state.passo = 5; st.rerun()
    elif st.session_state.passo == 5:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO E: FOLLOW-UP</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['Follow-up'] = st.text_area("1. Como faz o follow-up?")
        if st.button("Finalizar"): st.session_state.passo = 6; st.rerun()

# --- FINALIZAÇÃO ---
elif st.session_state.passo == 6:
    if st.session_state.perfil == 'cliente':
        with st.spinner("Enviando..."):
            pdf = gerar_pdf({"Gargalo (Causa Raiz)": ["Manual"]}, gerar_ishikawa_pdf())
            enviar_email(st.session_state.respostas, pdf)
        st.success("Diagnóstico concluído!")
    elif st.session_state.perfil == 'consultor':
        st.write("Dashboard VEDA.IA")
