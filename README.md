# 🤖 Agente Financeiro Inteligente com IA Generativa

## Contexto

Os assistentes virtuais no setor financeiro estão evoluindo de simples chatbots reativos para **agentes inteligentes e proativos**. Neste desafio, você vai idealizar e prototipar um agente financeiro que utiliza IA Generativa para:

- **Antecipar necessidades** ao invés de apenas responder perguntas
- **Personalizar** sugestões com base no contexto de cada cliente
- **Cocriar soluções** financeiras de forma consultiva
- **Garantir segurança** e confiabilidade nas respostas (anti-alucinação)

> [!TIP]
> Na pasta [`examples/`](./examples/) você encontra referências de implementação para cada etapa deste desafio.

---

## O Que Você Deve Entregar

### 1. Documentação do Agente

Defina **o que** seu agente faz e **como** ele funciona:

- **Caso de Uso:** Qual problema financeiro ele resolve? (ex: consultoria de investimentos, planejamento de metas, alertas de gastos)
- **Persona e Tom de Voz:** Como o agente se comporta e se comunica?
- **Arquitetura:** Fluxo de dados e integração com a base de conhecimento
- **Segurança:** Como evitar alucinações e garantir respostas confiáveis?

📄 **Template:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

Utilize os **dados mockados** disponíveis na pasta [`data/`](./data/) para alimentar seu agente:

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `transacoes.csv` | CSV | Histórico de transações do cliente |
| `historico_atendimento.csv` | CSV | Histórico de atendimentos anteriores |
| `perfil_investidor.json` | JSON | Perfil e preferências do cliente |
| `produtos_financeiros.json` | JSON | Produtos e serviços disponíveis |
| `simulacoes_financeiras.json` | JSON | Simulações Financeiras |
| `faq_financeiro.json` | JSON | Suporte ao Cliente |

## Expansão nos Dados

As expensões foram baseadas em um suporte melhor ao Cliente com o FAQ e também com Simulações Financeiras deixando mais prático sua vida.

### Como os dados são carregados

Existem duas opções, diretamente no Prompt ou através de código, como no exemplo abaixo:

```python
import pandas as pd
import json
import os

# Caminho base do projeto
BASE_DIR = "data"

def load_json(file_name):
    path = os.path.join(BASE_DIR, file_name)
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"[OK] JSON carregado: {file_name}")
            return data
    except FileNotFoundError:
        print(f"[ERRO] Arquivo não encontrado: {file_name}")
    except json.JSONDecodeError:
        print(f"[ERRO] JSON inválido: {file_name}")
    return None


def load_csv(file_name):
    path = os.path.join(BASE_DIR, file_name)
    try:
        df = pd.read_csv(path)
        print(f"[OK] CSV carregado: {file_name}")
        return df
    except FileNotFoundError:
        print(f"[ERRO] Arquivo não encontrado: {file_name}")
    except pd.errors.EmptyDataError:
        print(f"[ERRO] CSV vazio: {file_name}")
    return None


# Carregamento dos dados
produtos = load_json("produtos_financeiros.json")
simulacoes = load_json("simulacoes_financeiras.json")

transacoes = load_csv("transacoes.csv")
historico = load_csv("historico_atendimento.csv")


# Validação básica
if transacoes is not None:
    print("\nResumo das transações:")
    print(transacoes.describe())

if historico is not None:
    print("\nHistórico de atendimentos:")
    print(historico.head())
```

### Como os dados são usados no Prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

```
PERFIL E DADOS DO CLIENTE (data/perfil_investidor.json):
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

TRANSACOES DO CLIENTE (data/transacoes.csv):
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

FAQ FINANCEIRO (data/faq_financeiro.json):
[
  {
    "pergunta": "Quanto posso guardar por mês?",
    "resposta": "Com base nos seus dados, você possui aproximadamente R$ 2500 livres por mês, permitindo bons aportes para atingir suas metas financeiras."
  },
  {
    "pergunta": "Quanto falta para minha reserva de emergência?",
    "resposta": "Você já possui R$ 10.000 e precisa de R$ 15.000. Faltam R$ 5.000 para completar sua reserva."
  },
  {
    "pergunta": "Em quanto tempo consigo atingir minha meta?",
    "resposta": "Aportando R$ 500 por mês, você atinge sua meta em aproximadamente 10 meses."
  },
  {
    "pergunta": "Qual investimento combina com meu perfil?",
    "resposta": "Como seu perfil é moderado, opções como CDB e Tesouro Selic são adequadas para segurança e crescimento gradual."
  },
  {
    "pergunta": "Estou gastando muito?",
    "resposta": "Seu comprometimento de renda está em torno de 50%, o que é considerado saudável, mas pode ser otimizado para aumentar seus investimentos."
  },
  {
    "pergunta": "Qual meu maior gasto?",
    "resposta": "Seu maior gasto atual é com moradia (aluguel), seguido por alimentação."
  },
  {
    "pergunta": "Vale a pena investir ou guardar dinheiro?",
    "resposta": "Para seu objetivo de reserva de emergência, o ideal é investir em opções seguras com liquidez, como Tesouro Selic ou CDB com liquidez diária."
  },
  {
    "pergunta": "O que é Tesouro Selic?",
    "resposta": "É um título público de baixo risco indicado para reserva de emergência, com rendimento próximo à taxa Selic."
  }
]

HISTORICO DE ATENDIMENTO (data/historico_atendimento.csv):
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

PRODUTOS FINANCEIROS (data/produtos_financeiros.json):
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Multimercado",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI + 2%",
    "aporte_minimo": 500.00,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]

SIMULACOES FINANCEIRAS (data/simulacoes_financeiras.json):
{
  "juros_compostos": {
    "descricao": "Cálculo de rendimento ao longo do tempo com reinvestimento",
    "formula": "M = P * (1 + i)^n",
    "variaveis": {
      "P": "valor inicial",
      "i": "taxa de juros mensal",
      "n": "tempo em meses"
    },
    "exemplo_usuario": {
      "valor_inicial": 10000,
      "taxa": 0.01,
      "periodo_meses": 12,
      "resultado_aproximado": 11268
    }
  },

  "aporte_mensal": {
    "descricao": "Simula crescimento com aportes mensais",
    "formula": "M = P + (aporte * n)",
    "exemplo_usuario": {
      "aporte_mensal": 500,
      "periodo_meses": 10,
      "resultado": 15000,
      "contexto": "Usuário pode atingir a meta de reserva de emergência"
    }
  },

  "parcelamento": {
    "descricao": "Divisão simples de valores",
    "formula": "parcela = valor_total / numero_parcelas",
    "exemplo": {
      "valor_total": 1200,
      "parcelas": 6,
      "valor_parcela": 200
    }
  },

  "comprometimento_renda": {
    "descricao": "Calcula percentual da renda comprometida com despesas",
    "formula": "percentual = (despesas / renda) * 100",
    "exemplo_usuario": {
      "renda": 5000,
      "despesas": 2488,
      "percentual": 49.7
    }
  }
}
```

## Exemplo de Contexto Montado

> Exemplo de como os dados são formatados para o agente:

```
DADOS DO CLIENTE:
- Nome: João Silva
- Idade: 32
- Profissão: Analista de Sistemas
- Renda Mensal: R$ 5000.00
- Perfil de Investidor: Moderado
- Aceita Risco: Não
- Objetivo Principal: Construir reserva de emergência
- Patrimônio Total: R$ 15000.00
- Reserva de Emergência Atual: R$ 10000.00

METAS FINANCEIRAS:
- Completar reserva de emergência: R$ 15000.00 até 2026-06
- Entrada do apartamento: R$ 50000.00 até 2027-12

RESUMO FINANCEIRO:
- Total de Receitas: R$ 5000.00
- Total de Despesas: R$ 2488.90
- Saldo Mensal Disponível: R$ 2511.10
- Maior Categoria de Gasto: Moradia

DETALHAMENTO DE GASTOS:
- Moradia: R$ 1380.00
- Alimentação: R$ 570.00
- Transporte: R$ 295.00
- Saúde: R$ 188.00
- Lazer: R$ 55.90

HISTÓRICO DE INTERAÇÕES:
- [2025-10-12] Tema: Metas financeiras → Cliente acompanhou progresso da reserva
- [2025-10-01] Tema: Tesouro Selic → Cliente pediu explicação
- [2025-09-15] Tema: CDB → Cliente perguntou sobre rentabilidade

PRODUTOS FINANCEIROS RELEVANTES:
- Tesouro Selic → Baixo risco | Ideal para reserva de emergência
- CDB Liquidez Diária → Baixo risco | Rendimento diário
- Fundo Multimercado → Risco médio | Diversificação

REGRAS DE NEGÓCIO:
- Sempre considerar o perfil moderado do usuário
- Priorizar segurança e liquidez
- Evitar recomendações de alto risco
- Explicar cálculos de forma clara

SIMULAÇÕES DISPONÍVEIS:
- Juros Compostos → M = P * (1 + i)^n
- Aporte Mensal → Crescimento com depósitos mensais
- Parcelamento → Divisão de valores
- Comprometimento de Renda → (% renda comprometida)

FAQ RELEVANTE:
- Quanto posso guardar por mês? → Aproximadamente R$ 2500 livres
- Quanto falta para minha reserva? → Faltam R$ 5000
- Em quanto tempo atinjo minha meta? → Aproximadamente 10 meses com aportes de R$ 500
- Estou gastando muito? → Cerca de 50% da renda (saudável, mas pode otimizar)

INSTRUÇÕES AO AGENTE:
- Use os dados acima para responder
- Seja claro, direto e educativo
- Personalize as respostas
- Evite respostas genéricas
```


📄 **Template:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

Documente os prompts que definem o comportamento do seu agente:

- **System Prompt:** Instruções gerais de comportamento e restrições
- **Exemplos de Interação:** Cenários de uso com entrada e saída esperada
- **Tratamento de Edge Cases:** Como o agente lida com situações limite

📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

Desenvolva um **protótipo funcional** do seu agente:

- Chatbot interativo (sugestão: Streamlit, Gradio ou similar)
- Integração com LLM (via API ou modelo local)
- Conexão com a base de conhecimento

📁 **Pasta:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

Descreva como você avalia a qualidade do seu agente:

**Métricas Sugeridas:**
- Precisão/assertividade das respostas
- Taxa de respostas seguras (sem alucinações)
- Coerência com o perfil do cliente

📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Grave um **pitch de 3 minutos** (estilo elevador) apresentando:

- Qual problema seu agente resolve?
- Como ele funciona na prática?
- Por que essa solução é inovadora?

📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Ferramentas Sugeridas

Todas as ferramentas abaixo possuem versões gratuitas:

| Categoria | Ferramentas |
|-----------|-------------|
| **LLMs** | [ChatGPT](https://chat.openai.com/), [Copilot](https://copilot.microsoft.com/), [Gemini](https://gemini.google.com/), [Claude](https://claude.ai/), [Ollama](https://ollama.ai/) |
| **Desenvolvimento** | [Streamlit](https://streamlit.io/), [Gradio](https://www.gradio.app/), [Google Colab](https://colab.research.google.com/) |
| **Orquestração** | [LangChain](https://www.langchain.com/), [LangFlow](https://www.langflow.org/), [CrewAI](https://www.crewai.com/) |
| **Diagramas** | [Mermaid](https://mermaid.js.org/), [Draw.io](https://app.diagrams.net/), [Excalidraw](https://excalidraw.com/) |

---

## Estrutura do Repositório

```
📁 lab-agente-financeiro/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── historico_atendimento.csv     # Histórico de atendimentos (CSV)
│   ├── perfil_investidor.json        # Perfil do cliente (JSON)
│   ├── produtos_financeiros.json     # Produtos disponíveis (JSON)
│   └── transacoes.csv                # Histórico de transações (CSV)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── app.py                        # (exemplo de estrutura)
│
├── 📁 assets/                        # Imagens e diagramas
│   └── ...
│
└── 📁 examples/                      # Referências e exemplos
    └── README.md
```

---

## Dicas Finais

1. **Comece pelo prompt:** Um bom system prompt é a base de um agente eficaz
2. **Use os dados mockados:** Eles garantem consistência e evitam problemas com dados sensíveis
3. **Foque na segurança:** No setor financeiro, evitar alucinações é crítico
4. **Teste cenários reais:** Simule perguntas que um cliente faria de verdade
5. **Seja direto no pitch:** 3 minutos passam rápido, vá ao ponto
