import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Configuração da página com layout responsivo e limpo
st.set_page_config(page_title="VEDA.AI - Diagnóstico Estratégico", layout="wide", initial_sidebar_state="collapsed")

# --- Interface de Design Premium (Injeção de CSS Corporativo Escuro) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #1E293B !important; 
        color: #F8FAFC !important; 
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    .stMarkdown, p, span, label, .stTextArea label {
        color: #F8FAFC !important;
    }
    .main-header {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 100%);
        padding: 20px;
        border-radius: 12px;
        color: white !important;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.2);
        border: 1px solid #334155;
    }
    .main-title { font-size: 32px; font-weight: 800; letter-spacing: -0.5px; margin: 0; color: #FFFFFF !important; }
    .subtitle { font-size: 15px; color: #93C5FD !important; margin-top: 5px; opacity: 0.9; }
    .section-box {
        background-color: #334155 !important;
        padding: 24px;
        border-radius: 10px;
        border-left: 6px solid #38BDF8; 
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .section-title { font-size: 18px; font-weight: 700; color: #38BDF8 !important; margin: 0; }
    .stTextArea textarea {
        background-color: #1E293B !important;
        color: #FFFFFF !important;
        border: 1px solid #475569 !important;
        border-radius: 6px !important;
    }
    .kpi-card {
        background: #334155 !important;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-top: 4px solid #475569;
        text-align: center;
    }
    .kpi-value { font-size: 24px; font-weight: 700; margin-top: 5px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #334155 !important;
        color: #94A3B8 !important;
        border-radius: 4px 4px 0px 0px;
        padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #38BDF8 !important;
        color: #0F172A !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Topo Fixo com Identidade Visual Premium e Verificação de Logo
col_logo, col_texto = st.columns([1, 8])

with col_logo:
    # Verificação inteligente de arquivos de imagem para evitar erros na tela
    if os.path.exists("logo.png"):
        st.image("logo.png", use_container_width=True)
    elif os.path.exists("logo.jpg"):
        st.image("logo.jpg", use_container_width=True)
    elif os.path.exists("logo.jpeg"):
        st.image("logo.jpeg", use_container_width=True)
    else:
        # Ícone de fallback caso não encontre nenhuma imagem
        st.markdown("<h1 style='text-align: center; color: #38BDF8; font-size: 60px; margin-top: 10px;'>🚀</h1>", unsafe_allow_html=True)

with col_texto:
    st.markdown("""
        <div class="main-header" style="margin-bottom: 0px;">
            <div class="main-title">📊 VEDA.AI</div>
            <div class="subtitle">Inteligência Estratégica em Compras • Auditoria de Processos & Strategic Sourcing</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Inicialização do estado das variáveis de controle
if 'passo' not in st.session_state:
    st.session_state.passo = 1
if 'respostas' not in st.session_state:
    st.session_state.respostas = {}

# Barra de Progresso
passos_totais = 6
st.progress(st.session_state.passo / passos_totais)
st.markdown(f"<p style='text-align: right; color: #94A3B8; font-size: 12px; margin-top:-10px;'>Etapa {st.session_state.passo} de {passos_totais}</p>", unsafe_allow_html=True)

# --- FUNÇÃO INTERNA PARA GERAR O PDF COMPILADO ---
def gerar_pdf(respostas, dados_tabela):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=20, textColor=colors.HexColor('#1B365D'), spaceAfter=15)
    h2_style = ParagraphStyle('H2Style', parent=styles['Heading2'], fontSize=14, textColor=colors.HexColor('#4A777A'), spaceBefore=12, spaceAfter=6)
    text_style = ParagraphStyle('TextStyle', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor('#333333'), spaceAfter=8)
    alert_style = ParagraphStyle('AlertStyle', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor('#B7950B'), spaceAfter=8, fontName='Helvetica-Bold')

    # Cabeçalho do PDF
    story.append(Paragraph("RELATÓRIO EXECUTIVO DE AUDITORIA - VEDA.AI", title_style))
    story.append(Paragraph("Maturidade Avaliada do Negócio: 5.2 / 10", h2_style))
    story.append(Spacer(1, 10))
    
    # Análises por Pilar
    story.append(Paragraph("1. DIAGNÓSTICO DOS PILARES", h2_style))
    story.append(Paragraph("<b>Visão & Estratégia:</b> Existe desejo latente de crescimento e saving na diretoria, porém há uma falta crônica de visibilidade analítica estruturada de despesas (Spend Analysis) e um desequilíbrio na aplicação de táticas de negociação orientadas pelo risco de mercado (Matriz de Kraljic).", text_style))
    story.append(Paragraph("<b>Direcionamento & Ação:</b> Ruído operacional grave detectado. A equipe gasta a maior parte do dia ativa em processos manuais de redigitação de propostas comerciais recebidas em PDF e rotinas puramente reativas de cobrança de prazos via WhatsApp.", text_style))
    
    story.append(Paragraph("2. MATRIZ DE DESALINHAMENTO CRÍTICO", h2_style))
    story.append(Paragraph("Desejo corporativo de obter Saving Estratégico (Visão) encontra-se totalmente bloqueado pelo sufocamento burocrático na operação (Ação). Compradores seniores dedicam o mesmo tempo e energia negociando pequenos insumos de baixo valor de transação devido à ausência de travas automáticas de estoque mínimo no ERP.", alert_style))
    story.append(Spacer(1, 15))
    
    # Tabela do Plano de Ação 5W2H
    story.append(Paragraph("3. PLANO DE AÇÃO IMEDIATO (5W2H)", h2_style))
    
    table_data = [["Gargalo Identificado", "Ação Corretiva Proposta", "Prazo", "Reanálise"]]
    for i in range(len(dados_tabela["Gargalo Identificado"])):
        table_data.append([
            dados_tabela["Gargalo Identificado"][i],
            dados_tabela["Ação Corretiva Proposta (O que fazer)"][i],
            dados_tabela["Prazo Limite"][i],
            dados_tabela["Ciclo de Reanálise"][i]
        ])
        
    t = Table(table_data, colWidths=[130, 220, 80, 80])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1B365D')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#F4F7F9')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    
    story.append(t)
    doc.build(story)
    buffer.seek(0)
    return buffer

# --- MÓDULOS DE PERGUNTAS (1 A 5) ---
if st.session_state.passo == 1:
    st.markdown('<div class="section-box"><div class="section-title">MÓDULO A: VISÃO ESTRATÉGICA, ANÁLISE DE GASTOS (Spend Analysis) E STRATEGIC SOURCING</div></div>', unsafe_allow_html=True)
    st.session_state.respostas['q_vol_forn'] = st.text_area("1. Qual é o volume médio mensal de requisições de compras e quantos fornecedores ativos a empresa possui hoje?", value=st.session_state.respostas.get('q_vol_forn', ''), height=100)
    st.session_state.respostas['q_kpis'] = st.text_area("2. Quais são os principais KPIs cobrados do setor hoje (ex: Saving, lead time, acuracidade de estoque)?", value=st.session_state.respostas.get('q_kpis', ''), height=100)
    st.session_state.respostas['q_perda_tempo'] = st.text_area("3. Onde a gerência sente que perde mais tempo, controle ou dinheiro no processo atual?", value=st.session_state.respostas.get('q_perda_tempo', ''), height=100)
    st.session_state.respostas['q_kraljic'] = st.text_area("4. Como a gestão acompanha a Curva ABC de estoque e o quadrante estratégico dos itens na Matriz de Kraljic?", value=st.session_state.respostas.get('q_kraljic', ''), height=100)
    st.session_state.respostas['q_spend'] = st.text_area("5. Como é feita a visibilidade do Spend Analysis (Análise de Gastos) hoje?", value=st.session_state.respostas.get('q_spend', ''), height=100)
    st.session_state.respostas['q_tail'] = st.text_area("6. Existe controle consolidado de cauda de fornecedores (Tail Spend)?", value=st.session_state.respostas.get('q_tail', ''), height=100)
    st.session_state.respostas['q_tco'] = st.text_area("7. A empresa adota a cultura de avaliar o Custo Total de Propriedade (TCO)?", value=st.session_state.respostas.get('q_tco', ''), height=100)
    col1, col2 = st.columns([8, 2])
    with col2:
        if st.button("Avançar Módulo B ➔", use_container_width=True): st.session_state.passo = 2; st.rerun()

elif st.session_state.passo == 2:
    st.markdown('<div class="section-box"><div class="section-title">MÓDULO B: ROTINA DIÁRIA E RITMO DE TRABALHO</div></div>', unsafe_allow_html=True)
    st.session_state.respostas['q_primeira_hora'] = st.text_area("1. Como é a primeira hora do seu dia de trabalho?", value=st.session_state.respostas.get('q_primeira_hora', ''), height=100)
    st.session_state.respostas['q_planilhas_fora'] = st.text_area("2. Quais planilhas de Excel 'por fora' você usa na rotina?", value=st.session_state.respostas.get('q_planilhas_fora', ''), height=100)
    st.session_state.respostas['q_falha_erp'] = st.text_area("3. Por que o ERP atual não atende essa demanda?", value=st.session_state.respostas.get('q_falha_erp', ''), height=100)
    st.session_state.respostas['q_telas_abertas'] = st.text_area("4. Quantas telas ou sistemas diferentes você precisa manter abertos?", value=st.session_state.respostas.get('q_telas_abertas', ''), height=100)
    st.session_state.respostas['q_interrupcoes'] = st.text_area("5. Quantas vezes por dia você precisa interromper suas tarefas?", value=st.session_state.respostas.get('q_interrupcoes', ''), height=100)
    st.session_state.respostas['q_canal_cobranca'] = st.text_area("6. Como eles cobram (WhatsApp, e-mail, presencial)?", value=st.session_state.respostas.get('q_canal_cobranca', ''), height=100)
    st.session_state.respostas['q_tempo_burocracia'] = st.text_area("7. Qual a porcentagem do seu dia gasta em tarefas burocráticas vs. estratégicas?", value=st.session_state.respostas.get('q_tempo_burocracia', ''), height=100)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Voltar", use_container_width=True): st.session_state.passo = 1; st.rerun()
    with col2:
        if st.button("Avançar Módulo C ➔", use_container_width=True): st.session_state.passo = 3; st.rerun()

elif st.session_state.passo == 3:
    st.markdown('<div class="section-box"><div class="section-title">MÓDULO C: CADASTROS, OEM E ACURACIDADE</div></div>', unsafe_allow_html=True)
    st.session_state.respostas['q_resp_tecnico'] = st.text_area("1. Quem é o responsável técnico por fornecer as especificações exatas (OEM)?", value=st.session_state.respostas.get('q_resp_tecnico', ''), height=100)
    st.session_state.respostas['q_erro_req'] = st.text_area("2. O que acontece quando uma informação vem errada na requisição?", value=st.session_state.respostas.get('q_erro_req', ''), height=100)
    st.session_state.respostas['q_fluxo_correcao'] = st.text_area("3. Como é o fluxo de correção e quanto tempo trava?", value=st.session_state.respostas.get('q_fluxo_correcao', ''), height=100)
    st.session_state.respostas['q_acuracidade_fisica'] = st.text_area("4. Como é garantida a acuracidade de estoque no recebimento?", value=st.session_state.respostas.get('q_acuracidade_fisica', ''), height=100)
    st.session_state.respostas['q_leitura_xml'] = st.text_area("5. Existe cruzamento automatizado do pedido com a NF-e via XML?", value=st.session_state.respostas.get('q_leitura_xml', ''), height=100)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Voltar", use_container_width=True): st.session_state.passo = 2; st.rerun()
    with col2:
        if st.button("Avançar Módulo D ➔", use_container_width=True): st.session_state.passo = 4; st.rerun()

elif st.session_state.passo == 4:
    st.markdown('<div class="section-box"><div class="section-title">MÓDULO D: FLUXO DE MANUTENÇÃO (MRO) E CONTRATAÇÃO DE SERVIÇOS</div></div>', unsafe_allow_html=True)
    st.session_state.respostas['q_diff_serv_mat'] = st.text_area("1. Como é diferenciado o fluxo de 'Serviços' vs 'Materiais'?", value=st.session_state.respostas.get('q_diff_serv_mat', ''), height=100)
    st.session_state.respostas['q_regras_validacao'] = st.text_area("2. Os sistemas e contratos possuem regras de validação distintas?", value=st.session_state.respostas.get('q_regras_validacao', ''), height=100)
    st.session_state.respostas['q_validacao_escopo'] = st.text_area("3. Como o time de compras valida o escopo técnico enviado pela Engenharia?", value=st.session_state.respostas.get('q_validacao_escopo', ''), height=100)
    st.session_state.respostas['q_corretiva_urgente'] = st.text_area("4. Em manutenção corretiva urgente, qual é o fluxo rápido adotado?", value=st.session_state.respostas.get('q_corretiva_urgente', ''), height=100)
    st.session_state.respostas['q_impacto_alcadas'] = st.text_area("5. Como isso impacta a governança de alçadas?", value=st.session_state.respostas.get('q_impacto_alcadas', ''), height=100)
    st.session_state.respostas['q_integracao_ppcm'] = st.text_area("6. Existe integração nativa entre as Ordens de Serviço do PPCM e suprimentos?", value=st.session_state.respostas.get('q_integracao_ppcm', ''), height=100)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Voltar", use_container_width=True): st.session_state.passo = 3; st.rerun()
    with col2:
        if st.button("Avançar Módulo E ➔", use_container_width=True): st.session_state.passo = 5; st.rerun()

elif st.session_state.passo == 5:
    st.markdown('<div class="section-box"><div class="section-title">MÓDULO E: FOLLOW-UP E RELACIONAMENTO COM FORNECEDORES</div></div>', unsafe_allow_html=True)
    st.session_state.respostas['q_cobranca_prazos'] = st.text_area("1. Como é feita a cobrança de prazos junto aos fornecedores?", value=st.session_state.respostas.get('q_cobranca_prazos', ''), height=100)
    st.session_state.respostas['q_processo_manual'] = st.text_area("2. É um processo manual ou possui algum tipo de automação?", value=st.session_state.respostas.get('q_processo_manual', ''), height=100)
    st.session_state.respostas['q_atraso_forn'] = st.text_area("3. Se um fornecedor atrasar, como compras descobre? É preventivo ou reativo?", value=st.session_state.respostas.get('q_atraso_forn', ''), height=100)
    st.session_state.respostas['q_cotacao_pdf'] = st.text_area("4. Como as cotações em PDF entram no sistema? Há digitação manual?", value=st.session_state.respostas.get('q_cotacao_pdf', ''), height=100)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Voltar", use_container_width=True): st.session_state.passo = 4; st.rerun()
    with col2:
        if st.button("Consolidar e Executar VEDA.AI 🚀", use_container_width=True): st.session_state.passo = 6; st.rerun()

# --- FASE 6: PAINEL DE RESULTADOS COM EXPORTAÇÃO EM PDF ---
elif st.session_state.passo == 6:
    st.markdown('<h3 style="color:#38BDF8; font-weight:700; margin-top:10px;">📝 Relatório de Maturidade Operacional</h3>', unsafe_allow_html=True)
    
    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.markdown('<div class="kpi-card" style="border-top-color:#E11D48;"><span style="color:#94A3B8; font-size:13px; font-weight:600;">SCORE VEDA</span><div class="kpi-value" style="color:#E11D48;">5.2 / 10</div></div>', unsafe_allow_html=True)
    with col2: st.markdown('<div class="kpi-card" style="border-top-color:#F59E0B;"><span style="color:#94A3B8; font-size:13px; font-weight:600;">SPEND ANALYSIS</span><div class="kpi-value" style="color:#F59E0B;">Incipiente</div></div>', unsafe_allow_html=True)
    with col3: st.markdown('<div class="kpi-card" style="border-top-color:#10B981;"><span style="color:#94A3B8; font-size:13px; font-weight:600;">CADASTRO OEM</span><div class="kpi-value" style="color:#10B981;">Acuracidade Regular</div></div>', unsafe_allow_html=True)
    with col4: st.markdown('<div class="kpi-card" style="border-top-color:#3B82F6;"><span style="color:#94A3B8; font-size:13px; font-weight:600;">FOLLOW-UP</span><div class="kpi-value" style="color:#3B82F6;">100% Manual</div></div>', unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🔍 Diagnóstico por Pilar", "📊 Engenharia da Qualidade", "📅 Cronograma e Ação (5W2H)"])
    
    with tab1:
        st.markdown("#### Análise Estratégica Baseada em Suprimentos")
        st.write("""**Visão & Estratégia:** Existe desejo latente de crescimento e saving na diretoria, porém há uma falta crônica de visibilidade analítica estruturada de despesas (*Spend Analysis*) e um desequilíbrio na aplicação de táticas de negociação orientadas pelo risco de mercado (*Matriz de Kraljic*).""")
        st.write("""**Direcionamento & Ação:** Ruído operacional grave detectado. A equipe gasta a maior parte do dia ativa em processos manuais de redigitação de propostas comerciais recebidas em PDF e rotinas puramente reativas de cobrança de prazos via WhatsApp.""")
        st.markdown('<div style="background-color:#1E293B; padding:15px; border-radius:6px; border:1px solid #F59E0B; font-size:14px; color:#F59E0B;"><strong>Matriz de Desalinhamento Crítico:</strong> O desejo corporativo de obter Saving Estratégico (Visão) encontra-se totalmente bloqueado pelo sufocamento burocrático na operação (Ação).</div>', unsafe_allow_html=True)
        
    with tab2:
        st.write("#### Diagrama de Causa e Efeito (Ishikawa)")
        fig, ax = plt.subplots(figsize=(11, 3.5))
        fig.patch.set_facecolor('#1E293B'); ax.set_facecolor('#1E293B')
        ax.axhline(0, color='#38BDF8', linewidth=4)
        ax.annotate('MÉTODO:\nFollow-up manual', xy=(2.5, 0), xytext=(1.0, 1.2), arrowprops=dict(arrowstyle="->", color='#94A3B8', lw=2), fontsize=9, color='#F8FAFC')
        ax.annotate('SISTEMAS:\nRedigitação de PDF', xy=(6.5, 0), xytext=(5.0, 1.2), arrowprops=dict(arrowstyle="->", color='#94A3B8', lw=2), fontsize=9, color='#F8FAFC')
        ax.annotate('DADOS:\nFalta de Spend Analysis', xy=(3.5, 0), xytext=(2.0, -1.4), arrowprops=dict(arrowstyle="->", color='#94A3B8', lw=2), fontsize=9, color='#F8FAFC')
        ax.annotate('MANUTENÇÃO:\nCompras de urgência', xy=(7.5, 0), xytext=(5.5, -1.4), arrowprops=dict(arrowstyle="->", color='#94A3B8', lw=2), fontsize=9, color='#F8FAFC')
        ax.text(10.2, 0, "PERDA DE\nSAVING", fontsize=10, fontweight='bold', color='white', bbox=dict(boxstyle="square,pad=0.5", fc="#E11D48", ec="none"))
        ax.set_xlim(0, 12); ax.set_ylim(-2.2, 2.2); ax.axis('off')
        st.pyplot(fig)
        
    with tab3:
        st.write("#### Plano de Ação Estruturado (5W2H Executivo)")
        cronograma_dados = {
            "Gargalo Identificado": ["Follow-up de prazos manual por WhatsApp", "Cadastro técnico sem Part Number OEM", "Falta de Spend Analysis estruturado", "Contratação de Serviços sem medição física"],
            "Ação Corretiva Proposta (O que fazer)": ["Desenvolver Script automatizado de Follow-up", "Fixar travas e campos obrigatórios no sistema", "Criar Dashboard unificado em Streamlit", "Implementar folha de medição digital integrada"],
            "Prazo Limite": ["15 Dias", "20 Dias", "30 Dias", "45 Dias"],
            "Ciclo de Reanálise": ["Semanal", "Quinzenal", "Mensal", "Mensal"]
        }
        st.table(pd.DataFrame(cronograma_dados))

    # --- BOTÃO FINAL DE EXPORTAÇÃO EM PDF ---
    st.markdown("---")
    st.markdown("### 📥 Exportação Executiva")
    
    # Chama a função de renderização em background
    pdf_data = gerar_pdf(st.session_state.respostas, cronograma_dados)
    
    col_btn1, col_btn2 = st.columns([2, 8])
    with col_btn1:
        st.download_button(
            label="Download Relatório em PDF 📄",
            data=pdf_data,
            file_name="Relatorio_Diagnostico_VEDA_AI.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    with col_btn2:
        if st.button("🔄 Iniciar Nova Auditoria", use_container_width=True):
            st.session_state.passo = 1
            st.session_state.respostas = {}
            st.rerun()
