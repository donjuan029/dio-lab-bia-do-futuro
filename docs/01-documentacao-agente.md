# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitos usuários possuem dúvidas financeiras básicas em seu dia-a-dia, como cálculos de parcelas, 
rendimento de investimentos e até mesmo compreensão de produtos financeiros,
isso se deve a dificuldade da linguagem técnica, falta de personalização e acesso limitado a orientação
confiável.

Além disso, ferramentas tradicionais são pouco intuitivas trazendo dificuldades na experiência dos usuários.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente utiliza IA generativa para compreender perguntas de forma natural, identificando a intenção do
usuário e fornecando respostas claras e objetivas.

Sendo capaz de:

- Explicar conceitos financeiros de forma simples
- Simular cenários (juros, parcelas, rendimento)
- Adaptar respostas ao contexto da conversa
- Guiar o usuário com sugestões educativas

### Público-Alvo
> Quem vai usar esse agente?

- Pessoas com pouco conhecimento financeiro
- Usuários que desejam organizar melhor suas finanças
- Estudantes e iniciantes em educação financeira
- Clientes que buscam respostas rápidas e confiáveis

---

## Persona e Tom de Voz

### Nome do Agente
FinAI Assistant

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

O agente possuem esses comportamentos:

- Educativo
- Consultivo
- Claro e orientado à solução

Ele atua como um "mentor financeiro digital", ajudando o usuário a entender e tomar decisões com mais segurança.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

- Acessível
- Didático
- Levemente informal
- Evita termos técnicos complexos sem explicação

### Exemplos de Linguagem
- Saudação:
  "Olá! Sou o FinAI, como posso ajudar com suas finanças hoje?"
- Confirmação:
  "Entendi! Vou calcular isso para você."
- Erro/Limitação:
  "No momento não tenho essa informação específica, mas posso te ajudar a entender conceitos relacionados"

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD

A[Usuário] -->|Pergunta em linguagem natural| B[Interface]

B --> C[Processamento de Entrada]
C --> D[LLM - Interpretação da Intenção]

D --> E{Tipo de Solicitação}

E -->|FAQ / Dúvida| F[Base de Conhecimento]
E -->|Cálculo Financeiro| G[Módulo de Simulação]
E -->|Explicação de Produto| H[Motor Educacional]

F --> I[LLM - Geração de Resposta]
G --> I
H --> I

I --> J[Validação e Segurança]

J --> K{Resposta segura?}

K -->|Sim| L[Resposta Final]
K -->|Não| M[Mensagem de Limitação]

L --> N[Usuário]
M --> N
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Chatbot (CLI, Colab ou Streamlit) |
| LLM | GPT-4 / GPT-4.1-mini via API |
| Base de Conhecimento | Regras financeiras básicas e lógica de cálculo |
| Validação | Controle de respostas e prevenção de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Agente responde com base em regras e contexto da conversa
- [ ] Explicações incluem lógica do cálculo (transparência)
- [ ] Quando não sabe, admite limitação
- [ ] Evita recomendações financeiras diretas sem contexto

### Limitações Declaradas
> O que o agente NÃO faz?

- Não fornece aconselhamento financeiro profissional
- Não substitui consultores ou especialistas
- Não realiza análise de perfil de investimento avançada
- Não acessa dados bancários reais
- Não garante precisão absoluta em cenários complexos
