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
# ⚙️ CONFIGURAÇÕES DE E-MAIL (PREENCHIDAS)
# ==========================================
EMAIL_REMETENTE = "vesda.ai.analytics@gmail.com"
SENHA_DO_EMAIL = "dugn fhbu nrzy xweo"
EMAIL_PADRAO_CONSULTOR = "silviosileiravasconcelos@hotmail.com"
# ==========================================

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
    .main-header {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 100%);
        padding: 20px; border-radius: 12px; color: white !important; margin-bottom: 25px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.2); border: 1px solid #334155;
    }
    .main-title { font-size: 32px; font-weight: 800; letter-spacing: -0.5px; margin: 0; color: #FFFFFF !important; }
    .subtitle { font-size: 15px; color: #93C5FD !important; margin-top: 5px; opacity: 0.9; }
    .section-box {
        background-color: #334155 !important; padding: 24px; border-radius: 10px;
        border-left: 6px solid #38BDF8; margin-bottom: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .section-title { font-size: 18px; font-weight: 700; color: #38BDF8 !important; margin: 0; }
    .stTextArea textarea { background-color: #1E293B !important; color: #FFFFFF !important; border: 1px solid #475569 !important; border-radius: 6px !important; }
    .kpi-card { background: #334155 !important; padding: 20px; border-radius: 8px; border-top: 4px solid #475569; text-align: center; }
    .kpi-value { font-size: 24px; font-weight: 700; margin-top: 5px; }
    .stTabs [data-baseweb="tab"] { background-color: #334155 !important; color: #94A3B8 !important; border-radius: 4px 4px 0px 0px; padding: 10px 20px; }
    .stTabs [aria-selected="true"] { background-color: #38BDF8 !important; color: #0F172A !important; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Topo Fixo
st.markdown("""
    <div class="main-header" style="margin-bottom: 0px;">
        <div class="main-title">📊 VEDA.IA</div>
        <div class="subtitle">Inteligência Estratégica em Compras • Auditoria de Processos & Strategic Sourcing</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Inicialização de Variáveis
if 'perfil' not in st.session_state: st.session_state.perfil = 'cliente'
if 'passo' not in st.session_state: st.session_state.passo = 1
if 'respostas' not in st.session_state: st.session_state.respostas = {}

# --- MENU LATERAL (ÁREA DO CONSULTOR) ---
with st.sidebar:
    if st.session_state.perfil == 'cliente':
        st.markdown("<h3 style='color:#38BDF8;'>💼 Acesso Restrito</h3>", unsafe_allow_html=True)
        senha = st.text_input("Senha Admin", type="password")
        if st.button("Entrar", use_container_width=True):
            if senha == "vedaadmin":
                st.session_state.perfil = 'consultor'
                st.rerun()
            elif senha != "": st.error("Senha incorreta.")
    else:
        st.markdown("<h3 style='color:#10B981;'>👨‍💼 Painel do Consultor</h3>", unsafe_allow_html=True)
        novo_email = st.text_input("E-mail para receber os relatórios", value=EMAIL_CONSULTOR_ATUAL)
        if st.button("💾 Salvar E-mail", use_container_width=True):
            guardar_email_consultor(novo_email)
            st.success("E-mail atualizado!")
        if st.button("Pular para Dashboard 🚀", use_container_width=True):
            st.session_state.passo = 6
            st.rerun()
        if st.button("Sair (Modo Cliente)", use_container_width=True):
            st.session_state.perfil = 'cliente'
            st.session_state.passo = 1
            st.rerun()

# --- FUNÇÃO PARA GERAR GRÁFICO (Ishikawa) ---
def gerar_ishikawa_pdf():
    fig, ax = plt.subplots(figsize=(10, 3.5))
    fig.patch.set_facecolor('#FFFFFF'); ax.set_facecolor('#FFFFFF')
    ax.axhline(0, color='#1B365D', linewidth=4)
    ax.annotate('MÉTODO:\nFollow-up manual', xy=(2.5, 0), xytext=(1.0, 1.2), arrowprops=dict(arrowstyle="->", color='#4A777A', lw=2), fontsize=9, color='black')
    ax.annotate('SISTEMAS:\nRedigitação manual', xy=(6.5, 0), xytext=(5.0, 1.2), arrowprops=dict(arrowstyle="->", color='#4A777A', lw=2), fontsize=9, color='black')
    ax.annotate('DADOS:\nFalta de Spend Analysis', xy=(3.5, 0), xytext=(2.0, -1.4), arrowprops=dict(arrowstyle="->", color='#4A777A', lw=2), fontsize=9, color='black')
    ax.annotate('MANUTENÇÃO:\nCompras de MRO', xy=(7.5, 0), xytext=(5.5, -1.4), arrowprops=dict(arrowstyle="->", color='#4A777A', lw=2), fontsize=9, color='black')
    ax.text(10.2, 0, "PERDA DE\nSAVING", fontsize=10, fontweight='bold', color='white', bbox=dict(boxstyle="square,pad=0.5", fc="#A93226", ec="none"))
    ax.set_xlim(0, 12); ax.set_ylim(-2.2, 2.2); ax.axis('off')
    img_buffer = io.BytesIO()
    fig.savefig(img_buffer, format='png', bbox_inches='tight', dpi=150)
    img_buffer.seek(0); plt.close(fig)
    return img_buffer

# --- FUNÇÃO PARA GERAR PDF (Relatório Executivo) ---
def gerar_pdf(dados_tabela, ishikawa_buffer):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=20, textColor=colors.HexColor('#1B365D'), spaceAfter=15)
    h2_style = ParagraphStyle('H2Style', parent=styles['Heading2'], fontSize=14, textColor=colors.HexColor('#4A777A'), spaceBefore=12, spaceAfter=6)
    text_style = ParagraphStyle('TextStyle', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor('#333333'), spaceAfter=8)
    alert_style = ParagraphStyle('AlertStyle', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor('#B7950B'), spaceAfter=8, fontName='Helvetica-Bold')
    table_text = ParagraphStyle('TableText', parent=styles['Normal'], fontSize=9, leading=12, textColor=colors.HexColor('#333333'))
    table_header = ParagraphStyle('TableHeader', parent=styles['Normal'], fontSize=10, leading=12, textColor=colors.whitesmoke, fontName='Helvetica-Bold')

    story.append(Paragraph("RELATÓRIO EXECUTIVO DE AUDITORIA - VEDA.IA", title_style))
    story.append(Paragraph("Maturidade Avaliada: 5.2 / 10", h2_style))
    story.append(RLImage(ishikawa_buffer, width=460, height=160))
    story.append(Spacer(1, 15))
    story.append(Paragraph("4. PLANO DE AÇÃO DETALHADO", h2_style))
    
    headers = [Paragraph("Gargalo", table_header), Paragraph("Ação Corretiva", table_header), Paragraph("Prazo", table_header), Paragraph("Status", table_header)]
    table_data = [headers]
    for i in range(len(dados_tabela["Gargalo (Causa Raiz)"])):
        table_data.append([ Paragraph(dados_tabela["Gargalo (Causa Raiz)"][i], table_text), Paragraph(dados_tabela["Ação Corretiva (Descrição do Trabalho)"][i], table_text), Paragraph(dados_tabela["Prazo e Tempo Necessário"][i], table_text), Paragraph(dados_tabela["Status / Reanálise"][i], table_text) ])
        
    t = Table(table_data, colWidths=[110, 210, 100, 90])
    t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1B365D')), ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1'))]))
    story.append(t); doc.build(story); buffer.seek(0)
    return buffer

# --- FUNÇÃO PARA ENVIAR E-MAIL ---
def enviar_email(respostas, pdf_buffer):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = carregar_email_consultor()
    msg['Subject'] = "🚨 VEDA.IA: Novo Diagnóstico Finalizado"
    corpo = "Diagnóstico finalizado. Segue relatório anexo."
    msg.attach(MIMEText(corpo, 'plain'))
    anexo = MIMEApplication(pdf_buffer.read(), _subtype="pdf")
    anexo.add_header('Content-Disposition', 'attachment', filename="Relatorio_VEDA.pdf")
    msg.attach(anexo)
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(EMAIL_REMETENTE, SENHA_DO_EMAIL)
        servidor.send_message(msg)
        servidor.quit()
        return True
    except: return False

# --- FLUXO DE PERGUNTAS (Passos 1-5) ---
if st.session_state.passo <= 5:
    # A lógica de perguntas continua igual...
    # (Inserir os blocos anteriores de perguntas aqui)
    if st.button("Finalizar Auditoria", use_container_width=True): 
        st.session_state.passo = 6; st.rerun()

# --- FASE 6 ---
elif st.session_state.passo == 6:
    # Lógica de processamento e e-mail
    st.success("Diagnóstico concluído!")
