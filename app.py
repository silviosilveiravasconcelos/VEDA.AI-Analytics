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

st.set_page_config(page_title="VEDA.IA - Diagnóstico Estratégico", layout="wide", initial_sidebar_state="collapsed")

# --- CSS E ESTILIZAÇÃO ---
st.markdown("""
    <style>
    .stApp { background-color: #1E293B !important; color: #F8FAFC !important; }
    .hero-box { text-align: center; padding: 40px; background: #334155; border-radius: 20px; border-left: 6px solid #38BDF8; }
    .hero-title { font-size: 42px; font-weight: 900; color: #38BDF8; }
    .section-box { background-color: #334155 !important; padding: 24px; border-radius: 10px; border-left: 6px solid #38BDF8; margin-bottom: 25px; }
    .section-title { font-size: 20px; font-weight: 700; color: #38BDF8 !important; margin-bottom: 15px; }
    .stTextArea textarea { background-color: #1E293B !important; color: #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

# --- ESTADO INICIAL ---
if 'perfil' not in st.session_state: st.session_state.perfil = 'cliente'
if 'passo' not in st.session_state: st.session_state.passo = 0

# --- MENU LATERAL (ADMIN) ---
with st.sidebar:
    if st.session_state.perfil == 'cliente':
        senha = st.text_input("Senha Admin", type="password")
        if st.button("Logar Consultor"):
            if senha == "vedaadmin": st.session_state.perfil = 'consultor'; st.rerun()
    else:
        st.markdown("### 👨‍💼 Painel Consultor")
        novo_email = st.text_input("E-mail para relatório", value=EMAIL_CONSULTOR_ATUAL)
        if st.button("💾 Salvar"): guardar_email_consultor(novo_email)
        if st.button("Sair (Modo Cliente)"): st.session_state.perfil = 'cliente'; st.session_state.passo = 0; st.rerun()

# --- TELA DE BOAS VINDAS (PASSO 0) ---
if st.session_state.passo == 0:
    st.markdown("""
        <div class="hero-box">
            <h1 class="hero-title">Bem-vindo ao VEDA.IA</h1>
            <p>Nossa metodologia foi desenhada para transformar a complexidade das suas compras em performance estratégica.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 Agora vamos iniciar o teste...", use_container_width=True):
        st.session_state.passo = 1; st.rerun()

# --- LÓGICA DE PERGUNTAS E PDF (AQUI O SEU ROTEIRO COMPLETO) ---
elif st.session_state.passo <= 5:
    if 'respostas' not in st.session_state: st.session_state.respostas = {}
    
    if st.session_state.passo == 1:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO A: VISÃO ESTRATÉGICA</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['A1'] = st.text_area("1. Qual o volume mensal de requisições e fornecedores ativos?")
        st.session_state.respostas['A2'] = st.text_area("2. Quais os principais KPIs cobrados?")
        if st.button("Avançar"): st.session_state.passo = 2; st.rerun()
        
    elif st.session_state.passo == 2:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO B: ROTINA DIÁRIA</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['B1'] = st.text_area("1. Como é a sua rotina diária?")
        st.session_state.respostas['B2'] = st.text_area("2. Que planilhas paralelas usa?")
        if st.button("Avançar"): st.session_state.passo = 3; st.rerun()
        
    elif st.session_state.passo == 3:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO C: CADASTROS E OEM</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['C1'] = st.text_area("1. Quem é o responsável pelos dados OEM?")
        st.session_state.respostas['C2'] = st.text_area("2. Como garantem a acuracidade?")
        if st.button("Avançar"): st.session_state.passo = 4; st.rerun()

    elif st.session_state.passo == 4:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO D: MANUTENÇÃO (MRO)</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['D1'] = st.text_area("1. Diferença de Serviços vs Materiais?")
        st.session_state.respostas['D2'] = st.text_area("2. Como validam o escopo técnico?")
        if st.button("Avançar"): st.session_state.passo = 5; st.rerun()

    elif st.session_state.passo == 5:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO E: FOLLOW-UP</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['E1'] = st.text_area("1. Como é o follow-up com fornecedores?")
        if st.button("Finalizar"): st.session_state.passo = 6; st.rerun()

# --- FINALIZAÇÃO (ENVIO E SUCESSO) ---
elif st.session_state.passo == 6:
    st.success("Diagnóstico concluído!")
    # [A lógica de Enviar E-mail e Gerar PDF continua aqui]
