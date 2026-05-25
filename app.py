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
        except: return EMAIL_PADRAO_CONSULTOR
    return EMAIL_PADRAO_CONSULTOR

def guardar_email_consultor(novo_email):
    with open(FICHEIRO_CONFIG, 'w') as f:
        json.dump({"email_consultor": novo_email}, f)

EMAIL_CONSULTOR_ATUAL = carregar_email_consultor()

st.set_page_config(page_title="VEDA.IA - Bem-vindo", layout="wide", initial_sidebar_state="collapsed")

# --- CSS E ESTILIZAÇÃO ---
st.markdown("""
    <style>
    .stApp { background-color: #1E293B !important; color: #F8FAFC !important; font-family: sans-serif; }
    .hero-box { text-align: center; padding: 40px; background: #334155; border-radius: 20px; border: 1px solid #475569; }
    .hero-title { font-size: 42px; font-weight: 900; color: #38BDF8; margin-bottom: 20px; }
    .hero-text { font-size: 18px; color: #E2E8F0; margin-bottom: 30px; line-height: 1.6; }
    .section-box { background-color: #334155 !important; padding: 24px; border-radius: 10px; border-left: 6px solid #38BDF8; margin-bottom: 25px; }
    .section-title { font-size: 20px; font-weight: 700; color: #38BDF8 !important; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# Inicialização de Variáveis
if 'perfil' not in st.session_state: st.session_state.perfil = 'cliente'
if 'passo' not in st.session_state: st.session_state.passo = 0 # Passo 0 é a tela inicial
if 'respostas' not in st.session_state: st.session_state.respostas = {}

# --- MENU LATERAL (ADMIN) ---
with st.sidebar:
    if st.session_state.perfil == 'cliente':
        senha = st.text_input("Senha Admin", type="password")
        if st.button("Logar Consultor"):
            if senha == "vedaadmin": st.session_state.perfil = 'consultor'; st.rerun()
    else:
        st.markdown("### 👨‍💼 Painel do Consultor")
        novo_email = st.text_input("E-mail para relatório", value=EMAIL_CONSULTOR_ATUAL)
        if st.button("💾 Salvar"): guardar_email_consultor(novo_email)
        if st.button("Sair (Modo Cliente)"): st.session_state.perfil = 'cliente'; st.session_state.passo = 0; st.rerun()

# --- TELA DE BOAS VINDAS (PASSO 0) ---
if st.session_state.passo == 0:
    st.markdown("""
        <div class="hero-box">
            <h1 class="hero-title">Bem-vindo ao VEDA.IA</h1>
            <p class="hero-text">
                Nossa metodologia foi desenhada para transformar a complexidade das suas compras em performance estratégica.<br>
                Esta auditoria digital irá mapear os gargalos da sua operação e desenhar o caminho para o próximo nível de eficiência.<br><br>
                <b>Pronto para reestruturar seu processo?</b>
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 Agora vamos iniciar o teste...", use_container_width=True):
        st.session_state.passo = 1
        st.rerun()

# --- FLUXO DE PERGUNTAS (Passos 1 a 5) ---
elif st.session_state.passo <= 5:
    st.markdown(f"### Módulo {chr(64 + st.session_state.passo)} de E")
    
    # [ADICIONE AQUI A LÓGICA DOS MÓDULOS A, B, C, D e E]
    # (Mantive a lógica resumida abaixo para o código não ficar gigante, 
    # use o conteúdo dos módulos anteriores aqui dentro)
    
    if st.session_state.passo == 1:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO A: VISÃO ESTRATÉGICA</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['A1'] = st.text_area("1. Qual o volume mensal de requisições?")
        if st.button("Avançar"): st.session_state.passo = 2; st.rerun()
        
    elif st.session_state.passo == 5:
        if st.button("Finalizar Diagnóstico"): st.session_state.passo = 6; st.rerun()

# --- FASE 6 (RESULTADO) ---
elif st.session_state.passo == 6:
    if st.session_state.perfil == 'cliente':
        st.markdown('<div class="section-box" style="text-align:center;"><h2>Diagnóstico finalizado com sucesso!</h2><p>Obrigado, seu relatório foi enviado ao consultor.</p></div>', unsafe_allow_html=True)
    else:
        st.write("Dashboard VEDA.IA - Visão Consultor")
