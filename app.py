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
SENHA_DO_EMAIL = "vyxo pyxq gwdp jass"
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

st.set_page_config(page_title="VEDA.IA - Diagnóstico", layout="wide", initial_sidebar_state="collapsed")

# --- CSS E ESTILIZAÇÃO ---
st.markdown("""
    <style>
    .stApp { background-color: #1E293B !important; color: #F8FAFC !important; }
    .hero-box { text-align: center; padding: 40px; background: #334155; border-radius: 20px; border-left: 6px solid #38BDF8; margin-bottom: 25px; }
    .section-box { background-color: #334155 !important; padding: 24px; border-radius: 10px; border-left: 6px solid #38BDF8; margin-bottom: 25px; }
    .section-title { font-size: 20px; font-weight: 700; color: #38BDF8 !important; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# --- ESTADO ---
if 'perfil' not in st.session_state: st.session_state.perfil = 'cliente'
if 'passo' not in st.session_state: st.session_state.passo = 0
if 'respostas' not in st.session_state: st.session_state.respostas = {}
if 'cliente_info' not in st.session_state: st.session_state.cliente_info = {"nome": "", "empresa": ""}

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
        if st.button("Sair (Modo Cliente)"): st.session_state.perfil = 'cliente'; st.session_state.passo = 0; st.rerun()

# --- TELA DE BOAS VINDAS (PASSO 0) ---
if st.session_state.passo == 0:
    st.markdown('<div class="hero-box"><h1>Bem-vindo ao VEDA.IA</h1><p>Diagnóstico de Compras e Automação.</p></div>', unsafe_allow_html=True)
    st.session_state.cliente_info["nome"] = st.text_input("Seu nome:")
    st.session_state.cliente_info["empresa"] = st.text_input("Nome da sua empresa:")
    if st.button("🚀 Iniciar Diagnóstico"):
        if st.session_state.cliente_info["nome"] and st.session_state.cliente_info["empresa"]:
            st.session_state.passo = 1; st.rerun()
        else: st.warning("Por favor, preencha nome e empresa.")

# --- LÓGICA DE PERGUNTAS ---
elif st.session_state.passo <= 5:
    st.progress(st.session_state.passo / 5)
    
    if st.session_state.passo == 1:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO A: VISÃO ESTRATÉGICA</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['A1'] = st.text_area("1. Qual o volume mensal de requisições e fornecedores ativos?")
        st.session_state.respostas['A2'] = st.text_area("2. Quais os principais KPIs cobrados?")
        st.session_state.respostas['A3'] = st.text_area("3. Onde perde mais tempo/dinheiro?")
        st.session_state.respostas['A4'] = st.text_area("4. Como acompanham a Matriz de Kraljic?")
        st.session_state.respostas['A5'] = st.text_area("5. Como é a visibilidade do Spend Analysis?")
        st.session_state.respostas['A6'] = st.text_area("6. Existe controle de Tail Spend?")
        st.session_state.respostas['A7'] = st.text_area("7. Avaliam o TCO (Custo Total de Propriedade)?")
        if st.button("Avançar"): st.session_state.passo = 2; st.rerun()
    
    elif st.session_state.passo == 2:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO B: ROTINA E RITMO</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['B1'] = st.text_area("1. Como é a primeira hora do dia?")
        st.session_state.respostas['B2'] = st.text_area("2. Que planilhas paralelas usa?")
        st.session_state.respostas['B3'] = st.text_area("3. Por que o ERP atual não atende?")
        st.session_state.respostas['B4'] = st.text_area("4. Quantas telas mantém abertas?")
        st.session_state.respostas['B5'] = st.text_area("5. Quantas interrupções diárias?")
        st.session_state.respostas['B6'] = st.text_area("6. Como cobram (Zap, e-mail)?")
        st.session_state.respostas['B7'] = st.text_area("7. % Burocracia vs Estratégico?")
        if st.button("Avançar"): st.session_state.passo = 3; st.rerun()

    elif st.session_state.passo == 3:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO C: CADASTROS E OEM</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['C1'] = st.text_area("1. Quem é o responsável técnico (OEM)?")
        st.session_state.respostas['C2'] = st.text_area("2. Como tratam erros de requisição?")
        st.session_state.respostas['C3'] = st.text_area("3. Como é o fluxo de correção?")
        st.session_state.respostas['C4'] = st.text_area("4. Como garantem acuracidade no recebimento?")
        st.session_state.respostas['C5'] = st.text_area("5. Existe integração XML?")
        if st.button("Avançar"): st.session_state.passo = 4; st.rerun()

    elif st.session_state.passo == 4:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO D: MRO E SERVIÇOS</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['D1'] = st.text_area("1. Diferença de Serviços vs Materiais?")
        st.session_state.respostas['D2'] = st.text_area("2. Como validam escopo técnico?")
        st.session_state.respostas['D3'] = st.text_area("3. Integração com PPCM?")
        st.session_state.respostas['D4'] = st.text_area("4. Fluxo de corretiva urgente?")
        st.session_state.respostas['D5'] = st.text_area("5. Impacto nas alçadas?")
        if st.button("Avançar"): st.session_state.passo = 5; st.rerun()

    elif st.session_state.passo == 5:
        st.markdown('<div class="section-box"><div class="section-title">MÓDULO E: FOLLOW-UP</div></div>', unsafe_allow_html=True)
        st.session_state.respostas['E1'] = st.text_area("1. Como faz o follow-up?")
        st.session_state.respostas['E2'] = st.text_area("2. Como trata atrasos?")
        st.session_state.respostas['E3'] = st.text_area("3. Como insere cotações em PDF?")
        if st.button("Finalizar Diagnóstico"): st.session_state.passo = 6; st.rerun()

# --- FINALIZAÇÃO (PASSO 6) ---
elif st.session_state.passo == 6:
    if st.session_state.perfil == 'cliente':
        st.success(f"Obrigado, {st.session_state.cliente_info['nome']}! Dados enviados.")
    else:
        st.write("Dashboard VEDA.IA")
