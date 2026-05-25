import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Configuração da página com layout responsivo
st.set_page_config(page_title="VEDA.AI - Diagnóstico Estratégico", layout="wide", initial_sidebar_state="collapsed")

# --- Interface de Design Premium (Injeção de CSS Corporativo) ---
st.markdown("""
    <style>
    /* Configuração Geral do Fundo e Fonte */
    .stApp {
        background-color: #F8FAFC;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Topo e Títulos */
    .main-header {
        background: linear-gradient(135deg, #1B365D 0%, #2A4D7C 100%);
        padding: 30px;
        border-radius: 12px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
    }
    .main-title { font-size: 32px; font-weight: 800; letter-spacing: -0.5px; margin: 0; }
    .subtitle { font-size: 15px; color: #E2E8F0; margin-top: 5px; opacity: 0.9; }
    
    /* Caixa dos Módulos/Perguntas */
    .section-box {
        background-color: white;
        padding: 24px;
        border-radius: 10px;
        border-left: 6px solid #1B365D;
        margin-bottom: 25px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .section-title { font-size: 18px; font-weight: 700; color: #1B365D; margin: 0; }
    
    /* Estilização Customizada dos Inputs de Texto */
    .stTextArea textarea {
        background-color: #FCFDFE !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 6px !important;
        transition: all 0.2s ease-in-out;
    }
    .stTextArea textarea:focus {
        border-color: #1B365D !important;
        box-shadow: 0 0 0 3px rgba(27,54,93,0.1) !important;
    }
    
    /* Painéis de Indicadores / KPI Cards */
    .kpi-card {
        background: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        border-top: 4px solid #E2E8F0;
        text-align: center;
    }
    .kpi-value { font-size: 24px; font-weight: 700; margin-top: 5px; }
    
    /* Tabelas Executivas */
    .styled-table {
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
        font-size: 15px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
    </style>
""", unsafe_allow_html=True)

# Topo Fixo com Identidade Visual Premium
st.markdown("""
    <div class="main-header">
        <div class="main-title">📊 VEDA.AI</div>
        <div class="subtitle">Inteligência Estratégica em Compras • Auditoria de Processos & Strategic Sourcing</div>
    </div>
""", unsafe_allow_html=True)

# Inicialização do estado das variáveis de controle
if 'passo' not in st.session_state:
    st.session_state.passo = 1
if 'respostas' not in st.session_state:
    st.session_state.respostas = {}

# Barra de Progresso no estilo corporativo (fina e discreta)
passos_totais = 6
st.progress(st.session_state.passo / passos_totais)
st.markdown(f"<p style='text-align: right; color: #64748B; font-size: 12px; margin-top:-10px;'>Etapa {st.session_state.passo} de {passos_totais}</p>", unsafe_allow_html=True)

# --- FASE 1: MÓDULO A (VISÃO ESTRATÉGICA, SPEND ANALYSIS E STRATEGIC SOURCING) ---
if st.session_state.passo == 1:
    st.markdown('<div class="section-box"><div class="section-title">MÓDULO A: VISÃO ESTRATÉGICA, ANÁLISE DE GASTOS (Spend Analysis) E STRATEGIC SOURCING</div></div>', unsafe_allow_html=True)
    
    st.session_state.respostas['q_vol_forn'] = st.text_area(
        "1. Qual é o volume médio mensal de requisições de compras e quantos fornecedores ativos a empresa possui hoje?",
        value=st.session_state.respostas.get('q_vol_forn', ''), height=100
    )
    st.session_state.respostas['q_kpis'] = st.text_area(
        "2. Quais são os principais KPIs cobrados do setor hoje (ex: Saving, lead time, acuracidade de estoque)?",
        value=st.session_state.respostas.get('q_kpis', ''), height=100
    )
    st.session_state.respostas['q_perda_tempo'] = st.text_area(
        "3. Onde a gerência sente que perde mais tempo, controle ou dinheiro no processo atual?",
        value=st.session_state.respostas.get('q_perda_tempo', ''), height=100
    )
    st.session_state.respostas['q_kraljic'] = st.text_area(
        "4. Como a gestão acompanha a Curva ABC de estoque e o quadrante estratégico dos itens na Matriz de Kraljic? O esforço, tempo e o modelo de negociação da equipe de compras são diferenciados de acordo com a complexidade do mercado fornecedor (Itens Estratégicos, Alavancáveis, Gargalos ou de Transação)?",
        value=st.session_state.respostas.get('q_kraljic', ''), height=100
    )
    st.session_state.respostas['q_spend'] = st.text_area(
        "5. Como é feita a visibilidade do Spend Analysis (Análise de Gastos) hoje? Conseguimos extrair com clareza quem compra, o que compra, de quem compra e por quanto compra, mapeando o histórico por centro de custo, categoria de insumo e sazonalidade?",
        value=st.session_state.respostas.get('q_spend', ''), height=100
    )
    st.session_state.respostas['q_tail'] = st.text_area(
        "6. Existe controle consolidado de cauda de fornecedores (Tail Spend)? Que porcentagem do volume de compras é direcionada a fornecedores esporádicos ou de baixo impacto estratégico?",
        value=st.session_state.respostas.get('q_tail', ''), height=100
    )
    st.session_state.respostas['q_tco'] = st.text_area(
        "7. A empresa adota a cultura de avaliar o Custo Total de Propriedade (TCO - Total Cost of Ownership), mapeando custos ocultos além do preço bruto nominal da peça ou serviço (ex: custos de frete, impostos, manutenção, mobilização, combustível)?",
        value=st.session_state.respostas.get('q_tco', ''), height=100
    )

    col1, col2 = st.columns([8, 2])
    with col2:
        if st.button("Avançar Módulo B ➔", use_container_width=True):
            st.session_state.passo = 2
            st.rerun()

# --- FASE 2: MÓDULO B (ROTINA DIÁRIA E RITMO DE TRABALHO) ---
elif st.session_state.passo == 2:
    st.markdown('<div class="section-box"><div class="section-title">MÓDULO B: ROTINA DIÁRIA E RITMO DE TRABALHO (Foco: Operação/Compradores)</div></div>', unsafe_allow_html=True)
    
    st.session_state.respostas['q_primeira_hora'] = st.text_area(
        "1. Como é a primeira hora do seu dia de trabalho? Qual tela, sistema ou planilha você abre obrigatoriamente?",
        value=st.session_state.respostas.get('q_primeira_hora', ''), height=100
    )
    st.session_state.respostas['q_planilhas_fora'] = st.text_area(
        "2. Quais planilhas de Excel 'por fora' (controles paralelos) você usa na rotina?",
        value=st.session_state.respostas.get('q_planilhas_fora', ''), height=100
    )
    st.session_state.respostas['q_falha_erp'] = st.text_area(
        "3. Por que o ERP atual não atende essa demanda?",
        value=st.session_state.respostas.get('q_falha_erp', ''), height=100
    )
    st.session_state.respostas['q_telas_abertas'] = st.text_area(
        "4. Quantas telas, abas de navegador ou sistemas diferentes você precisa manter abertos para fechar uma única compra?",
        value=st.session_state.respostas.get('q_telas_abertas', ''), height=100
    )
    st.session_state.respostas['q_interrupcoes'] = st.text_area(
        "5. Quantas vezes por dia você precisa interromper suas tarefas para responder a cobranças de status de outros setores?",
        value=st.session_state.respostas.get('q_interrupcoes', ''), height=100
    )
    st.session_state.respostas['q_canal_cobranca'] = st.text_area(
        "6. Como eles cobram (WhatsApp, e-mail, presencial)?",
        value=st.session_state.respostas.get('q_canal_cobranca', ''), height=100
    )
    st.session_state.respostas['q_tempo_burocracia'] = st.text_area(
        "7. Se você pudesse cronometrar, qual a porcentagem do seu dia gasta em tarefas burocráticas (digitação, cobrança) vs. tarefas estratégicas (negociação e busca de novos parceiros)?",
        value=st.session_state.respostas.get('q_tempo_burocracia', ''), height=100
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Voltar", use_container_width=True): st.session_state.passo = 1; st.rerun()
    with col2:
        if st.button("Avançar Módulo C ➔", use_container_width=True): st.session_state.passo = 3; st.rerun()

# --- FASE 3: MÓDULO C (CADASTROS, OEM E ACURACIDADE) ---
elif st.session_state.passo == 3:
    st.markdown('<div class="section-box"><div class="section-title">MÓDULO C: CADASTROS, OEM E ACURACIDADE (Foco: Dados e Engenharia)</div></div>', unsafe_allow_html=True)
    
    st.session_state.respostas['q_resp_tecnico'] = st.text_area(
        "1. Quando uma necessidade de compra é gerada, quem é o responsável técnico por fornecer as especificações exatas (part numbers OEM, fabricante, desenhos técnicos)?",
        value=st.session_state.respostas.get('q_resp_tecnico', ''), height=100
    )
    st.session_state.respostas['q_erro_req'] = st.text_area(
        "2. O que acontece quando uma informação vem errada ou incompleta na requisição?",
        value=st.session_state.respostas.get('q_erro_req', ''), height=100
    )
    st.session_state.respostas['q_fluxo_correcao'] = st.text_area(
        "3. Como é o fluxo de correção e quanto tempo trava o processo?",
        value=st.session_state.respostas.get('q_fluxo_correcao', ''), height=100
    )
    st.session_state.respostas['q_acuracidade_fisica'] = st.text_area(
        "4. Como é garantida a acuracidade de estoque no recebimento físico?",
        value=st.session_state.respostas.get('q_acuracidade_fisica', ''), height=100
    )
    st.session_state.respostas['q_leitura_xml'] = st.text_area(
        "5. Existe cruzamento automatizado do pedido com a NF-e via leitura de arquivo XML?",
        value=st.session_state.respostas.get('q_leitura_xml', ''), height=100
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Voltar", use_container_width=True): st.session_state.passo = 2; st.rerun()
    with col2:
        if st.button("Avançar Módulo D ➔", use_container_width=True): st.session_state.passo = 4; st.rerun()

# --- FASE 4: MÓDULO D (FLUXO DE MANUTENÇÃO E SERVIÇOS) ---
elif st.session_state.passo == 4:
    st.markdown('<div class="section-box"><div class="section-title">MÓDULO D: FLUXO DE MANUTENÇÃO (MRO) E CONTRATAÇÃO DE SERVIÇOS</div></div>', unsafe_allow_html=True)
    
    st.session_state.respostas['q_diff_serv_mat'] = st.text_area(
        "1. Como é diferenciado o fluxo de contratação de 'Serviços' (mão de obra, locações) versus a compra de 'Materiais'?",
        value=st.session_state.respostas.get('q_diff_serv_mat', ''), height=100
    )
    st.session_state.respostas['q_regras_validacao'] = st.text_area(
        "2. Os sistemas e contratos possuem regras de validação distintas?",
        value=st.session_state.respostas.get('q_regras_validacao', ''), height=100
    )
    st.session_state.respostas['q_validacao_escopo'] = st.text_area(
        "3. Como o time de compras valida o escopo técnico (Escopo de Trabalho) enviado pela Engenharia/Manutenção para evitar aditivos de contrato tardios?",
        value=st.session_state.respostas.get('q_validacao_escopo', ''), height=100
    )
    st.session_state.respostas['q_corretiva_urgente'] = st.text_area(
        "4. No caso de manutenção corretiva (quebra de máquina/emergencial), qual é o fluxo rápido de compras adotado para reduzir o tempo de ociosidade operacional?",
        value=st.session_state.respostas.get('q_corretiva_urgente', ''), height=100
    )
    st.session_state.respostas['q_impacto_alcadas'] = st.text_area(
        "5. Como isso impacta a governança de alçadas?",
        value=st.session_state.respostas.get('q_impacto_alcadas', ''), height=100
    )
    st.session_state.respostas['q_integracao_ppcm'] = st.text_area(
        "6. Existe integração nativa entre o planejamento de manutenção (Ordens de Serviço do PPCM) e a abertura de requisições automáticas no setor de suprimentos?",
        value=st.session_state.respostas.get('q_integracao_ppcm', ''), height=100
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Voltar", use_container_width=True): st.session_state.passo = 3; st.rerun()
    with col2:
        if st.button("Avançar Módulo E ➔", use_container_width=True): st.session_state.passo = 5; st.rerun()

# --- FASE 5: MÓDULO E (FOLLOW-UP E RELACIONAMENTO) ---
elif st.session_state.passo == 5:
    st.markdown('<div class="section-box"><div class="section-title">MÓDULO E: FOLLOW-UP E RELACIONAMENTO COM FORNECEDORES</div></div>', unsafe_allow_html=True)
    
    st.session_state.respostas['q_cobranca_prazos'] = st.text_area(
        "1. Como é feita a cobrança de prazos junto aos fornecedores?",
        value=st.session_state.respostas.get('q_cobranca_prazos', ''), height=100
    )
    st.session_state.respostas['q_processo_manual'] = st.text_area(
        "2. É um processo manual (e-mail por e-mail, ligação por ligação) ou possui algum tipo de automação?",
        value=st.session_state.respostas.get('q_processo_manual', ''), height=100
    )
    st.session_state.respostas['q_atraso_forn'] = st.text_area(
        "3. Se um fornecedor atrasar uma entrega, como e quando compras descobre? O controle é preventivo (antes do vencimento) ou reativo?",
        value=st.session_state.respostas.get('q_atraso_forn', ''), height=100
    )
    st.session_state.respostas['q_cotacao_pdf'] = st.text_area(
        "4. Quando um fornecedor envia uma cotação em PDF, como esses valores entram no sistema? Há digitação manual item a item?",
        value=st.session_state.respostas.get('q_cotacao_pdf', ''), height=100
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Voltar", use_container_width=True): st.session_state.passo = 4; st.rerun()
    with col2:
        if st.button("Consolidar e Executar VEDA.AI 🚀", use_container_width=True): st.session_state.passo = 6; st.rerun()

# --- FASE 6: PAINEL EXECUTIVO DE DIAGNÓSTICO ---
elif st.session_state.passo == 6:
    st.markdown('<h3 style="color:#1B365D; font-weight:700;">📝 Relatório de Maturidade Operacional</h3>', unsafe_allow_html=True)
    
    # Grid Avançado de KPI Cards Corporativos
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="kpi-card" style="border-top-color:#A93226;"><span style="color:#64748B; font-size:13px; font-weight:600;">SCORE VEDA</span><div class="kpi-value" style="color:#A93226;">5.2 / 10</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="kpi-card" style="border-top-color:#F39C12;"><span style="color:#64748B; font-size:13px; font-weight:600;">SPEND ANALYSIS</span><div class="kpi-value" style="color:#F39C12;">Incipiente</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="kpi-card" style="border-top-color:#27AE60;"><span style="color:#64748B; font-size:13px; font-weight:600;">CADASTRO OEM</span><div class="kpi-value" style="color:#27AE60;">Acuracidade Regular</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="kpi-card" style="border-top-color:#2980B9;"><span style="color:#64748B; font-size:13px; font-weight:600;">FOLLOW-UP</span><div class="kpi-value" style="color:#2980B9;">100% Manual</div></div>', unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)

    # Abas Limpas e Modernas
    tab1, tab2, tab3 = st.tabs(["🔍 Diagnóstico por Pilar", "📊 Engenharia da Qualidade", "📅 Cronograma e Ação (5W2H)"])
    
    with tab1:
        st.markdown("#### Análise Estratégica Baseada em Suprimentos")
        st.write("""**Visão & Estratégia:** Existe desejo latente de crescimento e saving na diretoria, porém há uma falta crônica de visibilidade analítica estruturada de despesas (*Spend Analysis*) e um desequilíbrio na aplicação de táticas de negociação orientadas pelo risco de mercado (*Matriz de Kraljic*).""")
        st.write("""**Direcionamento & Ação:** Ruído operacional grave detectado. A equipe gasta a maior parte do dia ativa em processos manuais de redigitação de propostas comerciais recebidas em PDF e rotinas puramente reativas de cobrança de prazos via WhatsApp.""")
        
        st.markdown('<div style="background-color:#FEF9E7; padding:15px; border-radius:6px; border-left:4px solid #F39C12; font-size:14px;">'
                    '<strong>Matriz de Desalinhamento Crítico:</strong> O desejo corporativo de obter Saving Estratégico (Visão) encontra-se totalmente bloqueado pelo sufocamento burocrático na operação (Ação). Compradores seniores dedicam o mesmo tempo e energia negociando pequenos insumos de baixo valor de transação devido à ausência de travas automáticas de estoque mínimo no ERP.'
                    '</div>', unsafe_allow_html=True)
        
    with tab2:
        st.write("#### Diagrama de Causa e Efeito (Ishikawa) — Perda de Produtividade em Suprimentos")
        
        # Plotagem do Ishikawa ajustada para as cores do tema corporativo
        fig, ax = plt.subplots(figsize=(11, 4.5))
        fig.patch.set_facecolor('#F8FAFC')
        ax.set_facecolor('#F8FAFC')
        
        ax.axhline(0, color='#1B365D', linewidth=4)
        
        # Linhas guia do Ishikawa
        ax.annotate('MÉTODO:\nFollow-up manual e\nreativo com fornecedores', xy=(2.5, 0), xytext=(1.0, 1.2),
                    arrowprops=dict(arrowstyle="->", color='#4A777A', lw=2), fontsize=9)
        ax.annotate('SISTEMAS:\nRedigitação manual de cotações\nem PDF para o ERP', xy=(6.5, 0), xytext=(5.0, 1.2),
                    arrowprops=dict(arrowstyle="->", color='#4A777A', lw=2), fontsize=9)
        ax.annotate('DADOS:\nFalta de Spend Analysis\ne cadastros OEM falhos', xy=(3.5, 0), xytext=(2.0, -1.4),
                    arrowprops=dict(arrowstyle="->", color='#4A777A', lw=2), fontsize=9)
        ax.annotate('MANUTENÇÃO / SERVIÇOS:\nFalta de contratos de MRO\ngerando compras de urgência', xy=(7.5, 0), xytext=(5.5, -1.4),
                    arrowprops=dict(arrowstyle="->", color='#4A777A', lw=2), fontsize=9)
        
        # Cabeça do Diagrama (Efeito)
        ax.text(10.2, 0, "VAZAMENTO\nDE SAVING E\nEFICIÊNCIA", fontsize=10, fontweight='bold', color='white',
                bbox=dict(boxstyle="square,pad=0.5", fc="#A93226", ec="none"))
        
        ax.set_xlim(0, 12)
        ax.set_ylim(-2.2, 2.2)
        ax.axis('off')
        st.pyplot(fig)
        
    with tab3:
        st.write("#### Plano de Ação Estruturado (5W2H Executivo) com Ciclos de Reanálise")
        
        cronograma_dados = {
            "Gargalo Identificado": [
                "Follow-up de prazos manual por WhatsApp/E-mail",
                "Cadastro técnico de itens sem Part Number OEM",
                "Falta de visibilidade na cauda de gastos (Spend Analysis)",
                "Contratação de Serviços sem critérios e medições físicas"
            ],
            "Ação Corretiva Proposta (O que fazer)": [
                "Desenvolver Script automatizado de Follow-up integrado às datas do ERP",
                "Fixar travas e campos obrigatórios de fabricante no formulário de requisição",
                "Criar Dashboard em Streamlit consolidando histórico de XMLs de Notas Fiscais",
                "Implementar folha de medição digital integrada para prestadores"
            ],
            "Prazo Limite": ["15 Dias", "20 Dias", "30 Dias", "45 Dias"],
            "Ciclo de Reanálise": ["Semanal", "Quinzenal", "Mensal", "Mensal"]
        }
        
        df_plano = pd.DataFrame(cronograma_dados)
        st.table(df_plano)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Iniciar Nova Auditoria de Processo", use_container_width=True):
        st.session_state.passo = 1
        st.session_state.respostas = {}
        st.rerun()
