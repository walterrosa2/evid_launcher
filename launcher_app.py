import streamlit as st
import webbrowser

st.set_page_config(
    page_title="Valuation Hub",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS CUSTOMIZADO (Glassmorphism & Modern UI) ---
st.markdown("""
<style>
    /* Fundo geral (Gradiente sutil escuro) */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: white;
    }
    
    /* Configuração dos Cards */
    .card-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 30px;
        margin: 10px;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s;
        height: 100%;
        min-height: 280px;
        text-decoration: none;
        cursor: pointer;
    }
    
    .card-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.5);
        border-color: rgba(255, 255, 255, 0.3);
        background: rgba(255, 255, 255, 0.08);
    }

    /* Títulos e Textos */
    .card-title {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 10px;
        background: -webkit-linear-gradient(45deg, #60a5fa, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .card-desc {
        font-size: 0.95rem;
        color: #94a3b8;
        text-align: center;
        line-height: 1.5;
        margin-bottom: 20px;
    }

    /* Ícones ilustrativos (Emojis grandes por enquanto) */
    .card-icon {
        font-size: 4rem;
        margin-bottom: 15px;
    }
    
    /* Botão simulado */
    .card-btn {
        background: linear-gradient(90deg, #3b82f6 0%, #8b5cf6 100%);
        color: white;
        padding: 10px 24px;
        border-radius: 30px;
        font-weight: 600;
        text-decoration: none;
        border: none;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.3);
    }
    
    .card-btn:hover {
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.5);
        transform: scale(1.05);
    }

    /* Header Principal */
    .main-header {
        text-align: center;
        margin-bottom: 60px;
        margin-top: 20px;
    }
    
    .main-header h1 {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(to right, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    .main-header p {
        font-size: 1.2rem;
        color: #cbd5e1;
    }
    
    /* Remover elementos padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
col_logo_1, col_logo_2, col_logo_3 = st.columns([1, 1, 1])
with col_logo_2:
    st.image("logo_evid.png", use_container_width=True)

st.markdown("""
<div class="main-header">
    <h1>EVID IA</h1>
    <p>Central de Inteligência para Análise de Processos e Auditoria</p>
</div>
""", unsafe_allow_html=True)

# --- DEFINIÇÃO DOS PROJETOS (Portas configuradas conforme plano) ---
APPS = [
    {
        "name": "PDF Inteligente",
        "desc": "Análise profunda de PDFs e chatbot jurídico inteligente.",
        "icon": "🧠",
        "url": "https://pdf-inteligente-evid.up.railway.app/",
        "cta": "Abrir PDF Inteligente"
    },
    {
        "name": "Agente Mapeamento",
        "desc": "Mapeamento estrutural de documentos e extração de dados.",
        "icon": "�️",
        "url": "https://mapeamento-pericial.up.railway.app/",
        "cta": "Iniciar Mapeamento"
    },
    {
        "name": "Agente Catalogador",
        "desc": "Pipeline LLM para catalogação e organização de evidências.",
        "icon": "�",
        "url": "https://catalogador-pericial.up.railway.app/",
        "cta": "Abrir Catalogador"
    },
    {
        "name": "Paginador de Provas",
        "desc": "Inserção de paginação customizada em PDFs de processos.",
        "icon": "📄",
        "url": "https://evidpaginapdf-production.up.railway.app/",
        "cta": "Abrir Paginador"
    },
    {
        "name": "Extração de NFS-e",
        "desc": "Unificação e extração de dados de Notas Fiscais de Serviço.",
        "icon": "🧾",
        "url": "https://evidnfse-production.up.railway.app/",
        "cta": "Abrir Extrator NFSe"
    },
    {
        "name": "Plataforma Jurídica",
        "desc": "Consulta de processos, pessoas e instituições via API Escavador.",
        "icon": "⚖️",
        "url": "http://localhost:5000",
        "cta": "Acessar Plataforma"
    },
    {
        "name": "Respostas Quesitos",
        "desc": "Gerador de respostas a quesitos processuais com extração e consolidação.",
        "icon": "📝",
        "url": "http://localhost:8507",
        "cta": "Abrir Gerador"
    }
]

# --- RENDERIZAÇÃO DOS CARDS ---
# Definição de grade (max 4 por linha)
COLS_PER_ROW = 4

for i in range(0, len(APPS), COLS_PER_ROW):
    # Pega o lote da linha (ex: 0 a 4)
    row_apps = APPS[i : i + COLS_PER_ROW]
    
    # Cria as colunas SEMPRE no tamanho máximo para manter alinhamento
    cols = st.columns(COLS_PER_ROW)
    
    for j, app in enumerate(row_apps):
        with cols[j]:
            # Criando o card com link
            st.markdown(f"""
            <a href="{app['url']}" target="_blank" style="text-decoration:none;">
                <div class="card-container">
                    <div class="card-icon">{app['icon']}</div>
                    <div class="card-title">{app['name']}</div>
                    <div class="card-desc">{app['desc']}</div>
                    <div class="card-btn">{app['cta']}</div>
                </div>
            </a>
            """, unsafe_allow_html=True)
            
    # Espaçamento entre as linhas
    st.markdown("<br>", unsafe_allow_html=True)

# --- RODAPÉ ---
st.markdown("""
<div style="text-align: center; margin-top: 50px; color: #475569; font-size: 0.8rem;">
    Desenvolvido para Valuation • Ambiente Protegido
</div>
""", unsafe_allow_html=True)
