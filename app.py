import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Configuração da página do Streamlit
st.set_page_config(page_title="Consultoria V.E.D.A. - Diagnóstico", layout="wide")
st.title("📊 Sistema de Diagnóstico Estratégico - Método V.E.D.A.")
st.subheader("Ferramenta de Mapeamento Automatizado com Inteligência Artificial")

# Inicializar variáveis de estado para o questionário
if 'passo' not in st.session_state:
    st.session_state.passo = 1
if 'respostas' not in st.session_state:
    st.session_state.respostas = {}

# --- BLOCO DE PERGUNTAS ---
if st.session_state.passo == 1:
    st.header("Seção 1: [V] Visão e [E] Estratégia")
    q1 = st.text_area("1. Qual é a visão de futuro da empresa para os próximos 3 anos e quais as metas macro de faturamento/escala?", key="q1")
    q2 = st.text_area("2. Quais são as estratégias e diferenciais competitivos atuais para alcançar essa visão?", key="q2")
    q3 = st.text_area("3. Como é feito o Spend Analysis e o acompanhamento da Curva ABC de estoque/gastos hoje?", key="q3")
    
    if st.button("Avançar para Direcionamento e Ação ➔"):
        if q1 and q2 and q3:
            st.session_state.respostas['visao'] = q1
            st.session_state.respostas['estrategia'] = q2
            st.session_state.respostas['curva_abc'] = q3
            st.session_state.passo = 2
            st.rerun()
        else:
            st.error("Por favor, responda todas as perguntas para avançar.")

elif st.session_state.passo == 2:
    st.header("Seção 2: [D] Direcionamento e [A] Ação")
    q4 = st.text_area("4. Como as metas são desdobradas para a operação (Direcionamento) e quais KPIs medem o dia a dia?", key="q4")
    q5 = st.text_area("5. Descreva a rotina diária da operação: onde a equipe gasta mais tempo (Follow-up, MRO, cadastros OEM)?", key="q5")
    q6 = st.text_area("6. Como é feita a gestão e contratação de Serviços terceirizados e suas respectivas medições?", key="q6")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Voltar"):
            st.session_state.passo = 1
            st.rerun()
    with col2:
        if st.button("Gerar Diagnóstico Avançado com IA 🚀"):
            if q4 and q5 and q6:
                st.session_state.respostas['direcionamento'] = q4
                st.session_state.respostas['acao'] = q5
                st.session_state.respostas['servicos'] = q6
                st.session_state.passo = 3
                st.rerun()
            else:
                st.error("Por favor, responda todas as perguntas para consolidar o relatório.")

# --- PROCESSAMENTO E RELATÓRIO FINAL ---
elif st.session_state.passo == 3:
    st.header("📝 Relatório de Diagnóstico Estratégico V.E.D.A.")
    
    # Aqui o sistema simula a execução do seu PROMPT DE IA integrado
    # Em produção, você conecta ao SDK da API (ex: google-genai) passando o st.session_state.respostas
    
    st.success("Analise Concluída com Sucesso! Nível de Maturidade Atual: 6.5 / 10")
    
    # Renderização do Painel de Pilares
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Visão", "Forte", "Metas Claras")
    col2.metric("Estratégia", "Regular", "Gargalo no TCO")
    col3.metric("Direcionamento", "Frágil", "Falta KPI")
    col4.metric("Ação", "Crítico", "Burocracia Manual")
    
    st.subheader("1. NOTA GERAL DO NEGÓCIO")
    st.info("**6.5/10** - Maturidade intermediária. A liderança sabe onde quer chegar, mas a operação está soterrada por processos manuais.")
    
    # Visualização das Ferramentas da Qualidade
    st.markdown("---")
    st.subheader("📊 Ferramentas da Qualidade Aplicadas ao Diagnóstico")
    
    tab1, tab2 = st.tabs(["Espinha de Peixe (Causa e Efeito)", "Plano de Ação e Cronograma"])
    
    with tab1:
        st.write("### Diagrama de Ishikawa (Espinha de Peixe) - Causa do Desperdício de Tempo Operacional")
        # Desenho customizado do gráfico usando matplotlib
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.axhline(0, color='black', linewidth=3)
        # Linhas das causas
        ax.annotate('MÉTODOS\nFollow-up Manual', xy=(2, 0), xytext=(1, 1), arrowprops=dict(arrowstyle="->", lw=1.5))
        ax.annotate('SISTEMAS\nFalta de integração ERP', xy=(5, 0), xytext=(4, 1), arrowprops=dict(arrowstyle="->", lw=1.5))
        ax.annotate('MÃO DE OBRA\nBurocracia em MRO', xy=(3, 0), xytext=(2, -1), arrowprops=dict(arrowstyle="->", lw=1.5))
        ax.annotate('DADOS\nCadastro OEM Incompleto', xy=(6, 0), xytext=(5, -1), arrowprops=dict(arrowstyle="->", lw=1.5))
        # Cabeça do peixe
        ax.text(8.5, 0, "PERDA DE\nSAVING", fontsize=12, fontweight='bold', bbox=dict(boxstyle="square", fc="red", ec="black"))
        ax.set_xlim(0, 10)
        ax.set_ylim(-2, 2)
        ax.axis('off')
        st.pyplot(fig)
        
    with tab2:
        st.write("### Plano de Ação Imediato (5W2H Simplificado) - Próximos 30 Dias")
        plano_df = pd.DataFrame({
            "Ação Corretiva (O que)": [
                "Automatizar o Follow-up de Fornecedores",
                "Fixar travas para cadastros OEM no formulário",
                "Criar Painel unificado de Spend Analysis"
            ],
            "Responsável (Quem)": ["Consultor / TI", "Engenharia de Processos", "Gestor de Compras"],
            "Prazo Execução": ["Dias 1 a 15", "Dias 10 a 20", "Dias 15 a 30"],
            "Período de Reanálise": ["Semanal", "Quinzenal", "Mensal"]
        })
        st.table(plano_df)
        
    if st.button("🔄 Reiniciar Novo Diagnóstico"):
        st.session_state.passo = 1
        st.session_state.respostas = {}
        st.rerun()
