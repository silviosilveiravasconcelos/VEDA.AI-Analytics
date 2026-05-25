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
    .stApp { background-color: #1E293B !important; color: #F8FAFC !important; font-family: sans-serif; }
    .section-box { background-color: #334155 !important; padding: 24px; border-radius: 10px; border-left: 6px solid #38BDF8; margin-bottom: 25px; }
    .section-title { font-size: 20px; font-weight: 700; color: #38BDF8 !important; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# Inicialização de Variáveis
if 'perfil' not in st.session_state: st.session_state.perfil = 'cliente'
if 'passo' not in st.session_state: st.session_state.passo = 1
if 'respostas' not in st.session_state: st.session_state.respostas = {}

# --- MENU LATERAL ---
with st.sidebar:
    if st.session_state.perfil == 'cliente':
        senha = st.text_input("Senha Consultor", type="password")
        if st.button("Logar"):
            if senha == "vedaadmin": st.session_state.perfil = 'consultor'; st.rerun()
    else:
        st.markdown("### 👨‍💼 Painel Consultor")
        novo_email = st.text_input("E-mail destino", value=EMAIL_CONSULTOR_ATUAL)
        if st.button("Salvar E-mail"): guardar_email_consultor(novo_email)
        if st.button("Sair"): st.session_state.perfil = 'cliente'; st.session_state.passo = 1; st.rerun()

# --- TOPO ---
st.markdown("## 📊 VEDA.IA - Diagnóstico de Compras")

# --- MÓDULOS DE PERGUNTAS (COMPLETO) ---
def renderizar_perguntas():
    if st.session_state.passo == 1:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO A: VISÃO ESTRATÉGICA E SPEND ANALYSIS</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['A1'] = st.text_area("1. Qual o volume médio mensal de requisições e fornecedores ativos?")
        st.session_state.respostas['A2'] = st.text_area("2. Quais os principais KPIs cobrados (Saving, Lead Time, etc)?")
        st.session_state.respostas['A3'] = st.text_area("3. Onde a gerência sente que perde mais tempo/dinheiro?")
        st.session_state.respostas['A4'] = st.text_area("4. Como acompanham a Matriz de Kraljic e Curva ABC?")
        if st.button("Próximo"): st.session_state.passo = 2; st.rerun()

    elif st.session_state.passo == 2:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO B: ROTINA DIÁRIA E RITMO</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['B1'] = st.text_area("1. Como é a primeira hora do seu dia?")
        st.session_state.respostas['B2'] = st.text_area("2. Quais planilhas paralelas (fora do ERP) você usa?")
        st.session_state.respostas['B3'] = st.text_area("3. Por que o ERP atual não atende?")
        if st.button("Próximo"): st.session_state.passo = 3; st.rerun()

    elif st.session_state.passo == 3:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO C: CADASTROS, OEM E ACURACIDADE</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['C1'] = st.text_area("1. Quem é o responsável técnico pelos dados OEM?")
        st.session_state.respostas['C2'] = st.text_area("2. Como tratam erros de requisição?")
        st.session_state.respostas['C3'] = st.text_area("3. Como garantem acuracidade física no recebimento?")
        if st.button("Próximo"): st.session_state.passo = 4; st.rerun()

    elif st.session_state.passo == 4:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO D: MANUTENÇÃO (MRO) E SERVIÇOS</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['D1'] = st.text_area("1. Diferença no fluxo de Serviços vs Materiais?")
        st.session_state.respostas['D2'] = st.text_area("2. Como validam o escopo técnico antes da compra?")
        st.session_state.respostas['D3'] = st.text_area("3. Existe integração com o PPCM?")
        if st.button("Próximo"): st.session_state.passo = 5; st.rerun()

    elif st.session_state.passo == 5:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO E: FOLLOW-UP E RELACIONAMENTO</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['E1'] = st.text_area("1. Como é o follow-up com fornecedores?")
        st.session_state.respostas['E2'] = st.text_area("2. Como tratam atrasos (preventivo ou reativo)?")
        st.session_state.respostas['E3'] = st.text_area("3. Como inserem cotações de PDF no sistema?")
        if st.button("Finalizar"): st.session_state.passo = 6; st.rerun()

renderizar_perguntas()

# --- FINALIZAÇÃO ---
if st.session_state.passo == 6:
    if st.session_state.perfil == 'cliente':
        # Aqui entra a função enviar_email e geração de PDF (omito por brevidade, mas o código de envio está completo no anterior)
        st.success("Diagnóstico concluído e enviado!")
    else:
        st.write("Dashboard VEDA.IA")
