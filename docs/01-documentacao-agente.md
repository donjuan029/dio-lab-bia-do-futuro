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
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [ex: Chatbot em Streamlit] |
| LLM | [ex: GPT-4 via API] |
| Base de Conhecimento | [ex: JSON/CSV com dados do cliente] |
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] [ex: Agente só responde com base nos dados fornecidos]
- [ ] [ex: Respostas incluem fonte da informação]
- [ ] [ex: Quando não sabe, admite e redireciona]
- [ ] [ex: Não faz recomendações de investimento sem perfil do cliente]

### Limitações Declaradas
> O que o agente NÃO faz?

[Liste aqui as limitações explícitas do agente]
