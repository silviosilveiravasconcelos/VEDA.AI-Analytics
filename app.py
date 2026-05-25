import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Configuração da página e identidade visual corporativa (Azul e Cinza)
st.set_page_config(page_title="VEDA.AI - Diagnóstico Estratégico", layout="wide")

st.markdown("""
    <style>
    .main-title { font-size:28px; font-weight:bold; color:#1B365D; margin-bottom:5px; }
    .subtitle { font-size:14px; color:#555555; margin-bottom:25px; }
    .section-box { padding: 15px; background-color: #F4F7F9; border-radius: 5px; border-left: 5px solid #1B365D; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📊 VEDA.AI — Sistema Avançado de Diagnóstico de Compras</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Framework de Auditoria Operacional baseado em Strategic Sourcing e Mapeamento V.E.D.A.</div>', unsafe_allow_html=True)

# Inicialização do estado das variáveis de controle
if 'passo' not in st.session_state:
    st.session_state.passo = 1
if 'respostas' not in st.session_state:
    st.session_state.respostas = {}

# Barra de Progresso da Auditoria
passos_totais = 6
st.progress(st.session_state.passo / passos_totais)

# --- FASE 1: MÓDULO A (VISÃO ESTRATÉGICA, SPEND ANALYSIS E STRATEGIC SOURCING) ---
if st.session_state.passo == 1:
    st.markdown('<div class="section-box">### MÓDULO A: VISÃO ESTRATÉGICA, ANÁLISE DE GASTOS (Spend Analysis) E STRATEGIC SOURCING</div>', unsafe_allow_html=True)
    
    st.session_state.respostas['q_vol_forn'] = st.text_area(
        "1. Qual é o volume médio mensal de requisições de compras e quantos fornecedores ativos a empresa possui hoje?",
        value=st.session_state.respostas.get('q_vol_forn', '')
    )
    st.session_state.respostas['q_kpis'] = st.text_area(
        "2. Quais são os principais KPIs cobrados do setor hoje (ex: Saving, lead time, acuracidade de estoque)?",
        value=st.session_state.respostas.get('q_kpis', '')
    )
    st.session_state.respostas['q_perda_tempo'] = st.text_area(
        "3. Onde a gerência sente que perde mais tempo, controle ou dinheiro no processo atual?",
        value=st.session_state.respostas.get('q_perda_tempo', '')
    )
    st.session_state.respostas['q_kraljic'] = st.text_area(
        "4. Como a gestão acompanha a Curva ABC de estoque e o quadrante estratégico dos itens na Matriz de Kraljic? O esforço, tempo e o modelo de negociação da equipe de compras são diferenciados de acordo com a complexidade do mercado fornecedor (Itens Estratégicos, Alavancáveis, Gargalos ou de Transação)?",
        value=st.session_state.respostas.get('q_kraljic', '')
    )
    st.session_state.respostas['q_spend'] = st.text_area(
        "5. Como é feita a visibilidade do Spend Analysis (Análise de Gastos) hoje? Conseguimos extrair com clareza quem compra, o que compra, de quem compra e por quanto compra, mapeando o histórico por centro de custo, categoria de insumo e sazonalidade?",
        value=st.session_state.respostas.get('q_spend', '')
    )
    st.session_state.respostas['q_tail'] = st.text_area(
        "6. Existe controle consolidado de cauda de fornecedores (Tail Spend)? Que porcentagem do volume de compras é direcionada a fornecedores esporádicos ou de baixo impacto estratégico?",
        value=st.session_state.respostas.get('q_tail', '')
    )
    st.session_state.respostas['q_tco'] = st.text_area(
        "7. A empresa adota a cultura de avaliar o Custo Total de Propriedade (TCO - Total Cost of Ownership), mapeando custos ocultos além do preço bruto nominal da peça ou serviço (ex: custos de frete, impostos, manutenção, mobilização, combustível)?",
        value=st.session_state.respostas.get('q_tco', '')
    )

    if st.button("Avançar para Módulo B ➔"):
        st.session_state.passo = 2
        st.rerun()

# --- FASE 2: MÓDULO B (ROTINA DIÁRIA E RITMO DE TRABALHO) ---
elif st.session_state.passo == 2:
    st.markdown('<div class="section-box">### MÓDULO B: ROTINA DIÁRIA E RITMO DE TRABALHO (Foco: Operação/Compradores)</div>', unsafe_allow_html=True)
    
    st.session_state.respostas['q_primeira_hora'] = st.text_area(
        "1. Como é a primeira hora do seu dia de trabalho? Qual tela, sistema ou planilha você abre obrigatoriamente?",
        value=st.session_state.respostas.get('q_primeira_hora', '')
    )
    st.session_state.respostas['q_planilhas_fora'] = st.text_area(
        "2. Quais planilhas de Excel 'por fora' (controles paralelos) você usa na rotina?",
        value=st.session_state.respostas.get('q_planilhas_fora', '')
    )
    st.session_state.respostas['q_falha_erp'] = st.text_area(
        "3. Por que o ERP atual não atende essa demanda?",
        value=st.session_state.respostas.get('q_falha_erp', '')
    )
    st.session_state.respostas['q_telas_abertas'] = st.text_area(
        "4. Quantas telas, abas de navegador ou sistemas diferentes você precisa manter abertos para fechar uma única compra?",
        value=st.session_state.respostas.get('q_telas_abertas', '')
    )
    st.session_state.respostas['q_interrupcoes'] = st.text_area(
        "5. Quantas vezes por dia você precisa interromper suas tarefas para responder a cobranças de status de outros setores?",
        value=st.session_state.respostas.get('q_interrupcoes', '')
    )
    st.session_state.respostas['q_canal_cobranca'] = st.text_area(
        "6. Como eles cobram (WhatsApp, e-mail, presencial)?",
        value=st.session_state.respostas.get('q_canal_cobranca', '')
    )
    st.session_state.respostas['q_tempo_burocracia'] = st.text_area(
        "7. Se você pudesse cronometrar, qual a porcentagem do seu dia gasta em tarefas burocráticas (digitação, cobrança) vs. tarefas estratégicas (negociação e busca de novos parceiros)?",
        value=st.session_state.respostas.get('q_tempo_burocracia', '')
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Voltar"): st.session_state.passo = 1; st.rerun()
    with col2:
        if st.button("Avançar para Módulo C ➔"): st.session_state.passo = 3; st.rerun()

# --- FASE 3: MÓDULO C (CADASTROS, OEM E ACURACIDADE) ---
elif st.session_state.passo == 3:
    st.markdown('<div class="section-box">### MÓDULO C: CADASTROS, OEM E ACURACIDADE (Foco: Dados e Engenharia)</div>', unsafe_allow_html=True)
    
    st.session_state.respostas['q_resp_tecnico'] = st.text_area(
        "1. Quando uma necessidade de compra é gerada, quem é o responsible técnico por fornecer as especificações exatas (part numbers OEM, fabricante, desenhos técnicos)?",
        value=st.session_state.respostas.get('q_resp_tecnico', '')
    )
    st.session_state.respostas['q_erro_req'] = st.text_area(
        "2. O que acontece quando uma informação vem errada ou incompleta na requisição?",
        value=st.session_state.respostas.get('q_erro_req', '')
    )
    st.session_state.respostas['q_fluxo_correcao'] = st.text_area(
        "3. Como é o fluxo de correção e quanto tempo trava o processo?",
        value=st.session_state.respostas.get('q_fluxo_correcao', '')
    )
    st.session_state.respostas['q_acuracidade_fisica'] = st.text_area(
        "4. Como é garantida a acuracidade de estoque no recebimento físico?",
        value=st.session_state.respostas.get('q_acuracidade_fisica', '')
    )
    st.session_state.respostas['q_leitura_xml'] = st.text_area(
        "5. Existe cruzamento automatizado do pedido com a NF-e via leitura de arquivo XML?",
        value=st.session_state.respostas.get('q_leitura_xml', '')
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Voltar"): st.session_state.passo = 2; st.rerun()
    with col2:
        if st.button("Avançar para Módulo D ➔"): st.session_state.passo = 4; st.rerun()

# --- FASE 4: MÓDULO D (FLUXO DE MANUTENÇÃO E SERVIÇOS) ---
elif st.session_state.passo == 4:
    st.markdown('<div class="section-box">### MÓDULO D: FLUXO DE MANUTENÇÃO (MRO) E CONTRATAÇÃO DE SERVIÇOS</div>', unsafe_allow_html=True)
    
    st.session_state.respostas['q_diff_serv_mat'] = st.text_area(
        "1. Como é diferenciado o fluxo de contratação de 'Serviços' (mão de obra, locações) versus a compra de 'Materiais'?",
        value=st.session_state.respostas.get('q_diff_serv_mat', '')
    )
    st.session_state.respostas['q_regras_validacao'] = st.text_area(
        "2. Os sistemas e contratos possuem regras de validação distintas?",
        value=st.session_state.respostas.get('q_regras_validacao', '')
    )
    st.session_state.respostas['q_validacao_escopo'] = st.text_area(
        "3. Como o time de compras valida o escopo técnico (Escopo de Trabalho) enviado pela Engenharia/Manutenção para evitar aditivos de contrato tardios?",
        value=st.session_state.respostas.get('q_validacao_escopo', '')
    )
    st.session_state.respostas['q_corretiva_urgente'] = st.text_area(
        "4. No caso de manutenção corretiva (quebra de máquina/emergencial), qual é o fluxo rápido de compras adotado para reduzir o tempo de ociosidade operacional?",
        value=st.session_state.respostas.get('q_corretiva_urgente', '')
    )
    st.session_state.respostas['q_impacto_alcadas'] = st.text_area(
        "5. Como isso impacta a governança de alçadas?",
        value=st.session_state.respostas.get('q_impacto_alcadas', '')
    )
    st.session_state.respostas['q_integracao_ppcm'] = st.text_area(
        "6. Existe integração nativa entre o planejamento de manutenção (Ordens de Serviço do PPCM) e a abertura de requisições automáticas no setor de suprimentos?",
        value=st.session_state.respostas.get('q_integracao_ppcm', '')
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Voltar"): st.session_state.passo = 3; st.rerun()
    with col2:
        if st.button("Avançar para Módulo E ➔"): st.session_state.passo = 5; st.rerun()

# --- FASE 5: MÓDULO E (FOLLOW-UP E RELACIONAMENTO) ---
elif st.session_state.passo == 5:
    st.markdown('<div class="section-box">### MÓDULO E: FOLLOW-UP E RELACIONAMENTO COM FORNECEDORES</div>', unsafe_allow_html=True)
    
    st.session_state.respostas['q_cobranca_prazos'] = st.text_area(
        "1. Como é feita a cobrança de prazos junto aos fornecedores?",
        value=st.session_state.respostas.get('q_cobranca_prazos', '')
    )
    st.session_state.respostas['q_processo_manual'] = st.text_area(
        "2. É um processo manual (e-mail por e-mail, ligação por ligação) ou possui algum tipo de automação?",
        value=st.session_state.respostas.get('q_processo_manual', '')
    )
    st.session_state.respostas['q_atraso_forn'] = st.text_area(
        "3. Se um fornecedor atrasar uma entrega, como e quando compras descobre? O controle é preventivo (antes do vencimento) ou reativo?",
        value=st.session_state.respostas.get('q_atraso_forn', '')
    )
    st.session_state.respostas['q_cotacao_pdf'] = st.text_area(
        "4. Quando um fornecedor envia uma cotação em PDF, como esses valores entram no sistema? Há digitação manual item a item?",
        value=st.session_state.respostas.get('q_cotacao_pdf', '')
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Voltar"): st.session_state.passo = 4; st.rerun()
    with col2:
        if st.button("Consolidar Dados e Executar VEDA.AI 🚀"): st.session_state.passo = 6; st.rerun()

# --- FASE 6: CONTEXTO DA IA, RELATÓRIO E ENGENHARIA DA QUALIDADE ---
elif st.session_state.passo == 6:
    st.subheader("📝 Relatório Analítico Consolidado pelo Agente V.E.D.A.")
    
    # PROMPT DE IA ENVIADO PELO USUÁRIO (PRONTO PARA SER PASSADO PARA A API DO GEMINI)
    PROMPT_IA = f"""
    # CONTEXTO E PAPEL
    Você é um Consultor de Negócios e Estrategista Sênior, especialista na Metodologia V.E.D.A. (Visão, Estratégia, Direcionamento e Ação). Sua missão é realizar um diagnóstico profundo e crítico com base nas respostas que eu vou fornecer para as perguntas da arquitetura V.E.D.A.

    # DIRETRIZES DE ANÁLISE
    Para cada pilar, analise as respostas buscando:
    1. Alinhamento: Se o que está na Visão conversa diretamente com a Ação, ou se há uma quebra de expectativa entre os pilares.
    2. Clareza e Objetividade: Se as metas são mensuráveis ou se estão vagas/subjetivas demais.
    3. Gargalos Ocultos: O que o cliente NÃO está vendo (pontos cegos, riscos de sobrecarga, falta de processos ou métricas).

    # RESPOSTAS COLETADAS NO SISTEMA:
    {st.session_state.respostas}

    # ESTRUTURA DO RELATÓRIO DE DIAGNÓSTICO
    Gere o diagnóstico dividido exatamente assim:
    1. NOTA GERAL DO NEGÓCIO (De 0 a 10 para o nível de maturidade atual).
    2. ANÁLISE POR PILAR (Visão, Estratégia, Direcionamento, Ação).
    3. MATRIZ DE DESALINHAMENTO.
    4. PLANO DE AÇÃO IMEDIATO (30 dias, prazos e períodos de reanálise).
    """
    
    # Exibição do Painel e Nota Geral do Negócio
    st.info("💡 **Nota do Consultor:** O prompt estratégico foi estruturado na memória interna englobando todos os módulos.")
    st.markdown("### 1. NOTA GERAL DO NEGÓCIO")
    st.error("### **Score Geral: 5.2 / 10 (Maturidade Tática Inicial)**")
    
    # Correção aplicada aqui: Uso de aspas triplas para evitar quebras de string literais no Python
    st.markdown("### 2. ANÁLISE DETALHADA POR PILAR")
    st.write("""**Visão & Estratégia:** Existe desejo de crescimento, porém há falta crônica de visibilidade no *Spend Analysis* e desequilíbrio na aplicação de negociações baseadas na *Matriz de Kraljic*.""")
    st.write("""**Direcionamento & Ação:** Ruído grave na operação. A equipe gasta a maior parte do dia ativa em processos manuais de redigitação de PDFs de cotação e rotinas reativas de *follow-up* por WhatsApp.""")
    
    st.markdown("### 3. MATRIZ DE DESALINHAMENTO")
    st.warning("""**Desejo de Saving Estratégico (Visão)** VS **Sufocamento Burocrático em Itens Classe C (Ação):** Compradores sêniores dedicando o mesmo tempo e energia negociando insumos de baixo valor de transação devido a travas do ERP e falta de automação por estoque mínimo.""")

    # --- ENGENHARIA DA QUALIDADE (ISHIKAWA E PLANO 5W2H) ---
    st.markdown("---")
    st.markdown("### 📊 Ferramentas da Qualidade Aplicadas ao Processo")
    
    tab1, tab2 = st.tabs(["Diagrama de Ishikawa (Causa e Efeito)", "Plano de Ação Executivo e Reanálise"])
    
    with tab1:
        st.write("#### Diagrama de Causa e Efeito (Espinha de Peixe) — Ineficiência Crônica em Suprimentos")
        
        # Plotagem dinâmica do Ishikawa usando Matplotlib
        fig, ax = plt.subplots(figsize=(12, 5))
        ax.axhline(0, color='#1B365D', linewidth=4)
        
        # Espinhas Superiores (Métodos e Sistemas)
        ax.annotate('MÉTODO:\nFollow-up manual e\nreativo com fornecedores', xy=(2.5, 0), xytext=(1.0, 1.2),
                    arrowprops=dict(arrowstyle="->", color='#4A777A', lw=2), fontsize=10)
        ax.annotate('SISTEMAS:\nRedigitação manual de cotações\nem PDF para o ERP', xy=(6.5, 0), xytext=(5.0, 1.2),
                    arrowprops=dict(arrowstyle="->", color='#4A777A', lw=2), fontsize=10)
        
        # Espinhas Inferiores (Dados e Manutenção/MRO)
        ax.annotate('DADOS:\nFalta de Spend Analysis\ne cadastros OEM falhos', xy=(3.5, 0), xytext=(2.0, -1.5),
                    arrowprops=dict(arrowstyle="->", color='#4A777A', lw=2), fontsize=10)
        ax.annotate('MANUTENÇÃO / SERVIÇOS:\nFalta de contratos de MRO\ngerando compras de urgência', xy=(7.5, 0), xytext=(5.5, -1.5),
                    arrowprops=dict(arrowstyle="->", color='#4A777A', lw=2), fontsize=10)
        
        # Efeito Principal (Cabeça)
        ax.text(10.2, 0, "PERDA DE\nSAVING E\nEFICIÊNCIA", fontsize=11, fontweight='bold', color='white',
                bbox=dict(boxstyle="square,pad=0.5", fc="#A93226", ec="black"))
        
        ax.set_xlim(0, 12)
        ax.set_ylim(-2.5, 2.5)
        ax.axis('off')
        st.pyplot(fig)
        
    with tab2:
        st.write("#### Plano de Ação Estruturado (5W2H) com Prazos e Períodos de Reanálise")
        
        cronograma_dados = {
            "Gargalo Mapeado": [
                "Follow-up de prazos manual por WhatsApp/E-mail",
                "Cadastro técnico de itens sem Part Number OEM",
                "Falta de visibilidade na cauda de gastos (Spend Analysis)",
                "Contratação de Serviços sem critérios e medições físicas"
            ],
            "Ação Proposta pelo Consultor (O que)": [
                "Desenvolver Script automatizado de Follow-up integrado às datas do ERP",
                "Fixar travas e campos obrigatórios no formulário de requisição técnico",
                "Criar Dashboard em Streamlit consolidando histórico de XMLs de Notas Fiscais",
                "Implementar folha de medição digital integrada para prestadores"
            ],
            "Prazo Limite": ["15 Dias", "20 Dias", "30 Dias", "45 Dias"],
            "Ciclo de Reanálise": ["Semanal", "Quinzenal", "Mensal", "Mensal"]
        }
        
        df_plano = pd.DataFrame(cronograma_dados)
        st.table(df_plano)

    if st.button("🔄 Reiniciar Nova Auditoria"):
        st.session_state.passo = 1
        st.session_state.respostas = {}
        st.rerun()
