import pandas as pd
import json
import os
import logging
import requests
import streamlit as st

# =========================
# CONFIGURAÇÃO
# =========================

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# Configuração de logs
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

# Caminho base
BASE_DIR = "data"


def load_json(file_name):
    path = os.path.join(BASE_DIR, file_name)

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

            if not data:
                raise ValueError("JSON vazio")

            logging.info(f"JSON carregado: {file_name}")
            return data

    except FileNotFoundError:
        logging.error(f"Arquivo não encontrado: {file_name}")
    except json.JSONDecodeError:
        logging.error(f"JSON inválido: {file_name}")
    except ValueError as e:
        logging.error(f"{file_name}: {e}")

    return None


def load_csv(file_name):
    path = os.path.join(BASE_DIR, file_name)

    try:
        df = pd.read_csv(path)

        if df.empty:
            raise ValueError("CSV vazio")

        logging.info(f"CSV carregado: {file_name}")
        return df

    except FileNotFoundError:
        logging.error(f"Arquivo não encontrado: {file_name}")
    except pd.errors.EmptyDataError:
        logging.error(f"CSV vazio: {file_name}")
    except Exception as e:
        logging.error(f"Erro ao carregar {file_name}: {e}")

    return None


# =========================
# CARREGAMENTO DOS DADOS
# =========================

# CSVs
transacoes = load_csv("transacoes.csv")
historico = load_csv("historico_atendimento.csv")

# JSONs
perfil = load_json("perfil_investidor.json")
produtos = load_json("produtos_financeiros.json")
simulacoes = load_json("simulacoes_financeiras.json")
faq = load_json("faq_financeiro.json")

# =========================
# MONTAR CONTEXTO
# =========================

contexto = f"""
================ DADOS DO CLIENTE ================

Nome: {perfil['nome']}
Idade: {perfil['idade']} anos
Profissão: {perfil['profissao']}
Perfil de Investidor: {perfil['perfil_investidor']}
Aceita Risco: {"Sim" if perfil['aceita_risco'] else "Não"}

Objetivo Principal:
- {perfil['objetivo_principal']}

Patrimônio Total:
- R$ {perfil['patrimonio_total']}

Reserva de Emergência Atual:
- R$ {perfil['reserva_emergencia_atual']}

================ METAS FINANCEIRAS ================

{json.dumps(perfil['metas'], indent=2, ensure_ascii=False)}

================ TRANSAÇÕES RECENTES ================

{transacoes.to_string(index=False)}

================ HISTÓRICO DE ATENDIMENTOS ================

{historico.to_string(index=False)}

================ PRODUTOS FINANCEIROS ================

{json.dumps(produtos, indent=2, ensure_ascii=False)}

================ SIMULAÇÕES FINANCEIRAS ================

{json.dumps(simulacoes, indent=2, ensure_ascii=False)}

================ FAQ FINANCEIRO ================

{json.dumps(faq, indent=2, ensure_ascii=False)}

================ REGRAS DO AGENTE ================

- Sempre utilizar os dados reais do cliente
- Nunca inventar informações financeiras
- Priorizar segurança financeira
- Adaptar respostas ao perfil do usuário
- Explicar cálculos de forma didática
- Não recomendar investimentos incompatíveis com o perfil
- Se não souber algo, admitir limitação

===================================================
"""


# =========================
# VALIDAÇÃO BÁSICA
# =========================

if perfil:
    logging.info("\nPerfil do Cliente:")
    logging.info(perfil)

if transacoes is not None:
    logging.info("\nResumo das Transações:")
    logging.info(transacoes.describe())

if historico is not None:
    logging.info("\nÚltimos Atendimentos:")
    logging.info(historico.tail(3))

if produtos:
    logging.info(f"\nProdutos disponíveis: {len(produtos)}")

if faq:
    logging.info(f"FAQs carregadas: {len(faq)}")

if simulacoes:
    logging.info(f"Simulações disponíveis: {list(simulacoes.keys())}")


# =========================
# SYSTEM PROMPT
# =========================


SYSTEM_PROMPT = """Você é o FinAI Assistant, um agente financeiro inteligente especializado em educação financeira, análise de gastos e simulações financeiras.

Seu objetivo é ajudar o usuário a entender melhor sua situação financeira, tomar decisões conscientes e atingir seus objetivos com segurança, clareza e personalização.

Você possui acesso aos dados reais do usuário, incluindo:
- Perfil financeiro
- Histórico de transações
- Metas financeiras
- Histórico de interações
- Produtos financeiros disponíveis
- Regras de simulação financeira

---

🎯 DIRETRIZES PRINCIPAIS:

- Sempre utilize os dados fornecidos para personalizar suas respostas
- Explique conceitos financeiros de forma simples e didática
- Seja claro, objetivo e útil
- Priorize segurança financeira e liquidez
- Adapte suas respostas ao perfil do usuário (moderado)

---

📊 USO DOS DADOS:

- Use o resumo financeiro para analisar gastos e sugerir melhorias
- Use as metas para orientar decisões e simulações
- Use o histórico para manter contexto e continuidade
- Use os produtos financeiros apenas se forem compatíveis com o perfil
- Use as simulações para explicar cálculos sempre que possível

---

⚠️ REGRAS DE SEGURANÇA (ANTI-ALUCINAÇÃO):

1. Nunca invente valores, dados ou informações
2. Nunca faça recomendações financeiras arriscadas
3. Nunca sugira investimentos incompatíveis com o perfil do usuário
4. Se não souber algo, diga claramente e ofereça ajuda alternativa
5. Não substitua um consultor financeiro profissional

---

💬 ESTILO DE RESPOSTA:

- Use linguagem acessível e amigável
- Evite termos técnicos sem explicação
- Sempre que possível:
  - Mostre cálculos
  - Explique o raciocínio
  - Dê exemplos práticos

---

📈 COMPORTAMENTO INTELIGENTE:

- Se o usuário perguntar sobre metas → use os dados de metas
- Se perguntar sobre gastos → analise as transações
- Se perguntar sobre investimentos → filtre pelo perfil (moderado)
- Se perguntar "posso guardar mais?" → use saldo mensal
- Se perguntar "vale a pena?" → explique prós e contras

---

🚫 LIMITAÇÕES:

- Não acessar dados externos
- Não prever mercado financeiro
- Não garantir rentabilidade futura
- Não tomar decisões pelo usuário

---

🎯 OBJETIVO FINAL:

Ajudar o usuário a:
- Entender sua situação financeira
- Melhorar seus hábitos
- Tomar decisões seguras
- Alcançar seus objetivos financeiros"""

# =========================
# CHAMAR OLLAMA
# =========================

def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# =========================
# INTERFACE
# =========================

st.title("Eu sou o FinAI Assistant")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
