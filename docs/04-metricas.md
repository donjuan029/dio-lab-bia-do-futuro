# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** 450,00 (supermercado) + 120,00 (restaurante) = 570,00 Valor baseado no `transacoes.csv`
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** 
Olá João!
Vamos escolher um investimento que seja seguro, com liquidez diária e que te ajude a atingir a meta da reserva de emergência (R$ 15 000) o mais rápido possível, sem arriscar seu capital.

1️⃣ Qual investimento?
Produto	Por que é indicado para você	Características principais
Tesouro Selic	- Baixo risco (título público)<br>- Rendimento próximo à Selic (pouco volátil)<br>- Liquidez diária (pode resgatar a qualquer momento)	- Aporte mínimo: R$ 30 <br>- Renda aproximada: 100 % da Selic (≈ 0,50 % ao mês, dependendo da taxa)
CDB Liquidez Diária	- Renda fixa, também de baixo risco<br>- Liquidez diária<br>- Rentabilidade superior ao Tesouro Selic (≈ 102 % do CDI)	- Aporte mínimo: R$ 100 <br>- Renda aproximada: 102 % do CDI (≈ 0,55 % ao mês, dependendo do CDI)
Recomendação prática: Comece com Tesouro Selic. Ele é mais simples de acompanhar, tem risco praticamente zero e já atende ao objetivo de reserva de emergência. Se quiser um rendimento ligeiramente melhor e não se importar com um prazo de carência de alguns dias (casas de investimento costumam exigir), pode complementar com um CDB Liquidez Diária.

2️⃣ Como calcular o crescimento da sua reserva
Supondo que você vá investir R$ 1.000,00 por mês no Tesouro Selic (ou CDB) e considerando a taxa de 0,50 % ao mês (Tesouro Selic), vamos usar a fórmula de juros compostos:

[ M = P \times (1+i)^n ]

Variável	Valor
(P) – capital inicial	R$ 10.000,00
(i) – taxa mensal	0,005 (0,50 %)
(n) – número de meses	10
[ M = 10.000 \times (1+0,005)^{10} \approx 10.000 \times 1,0510 \approx R$,10.510,00 ]

Depois de 10 meses, o valor composto seria ~R$ 10.510,00.

Adicione os aportes mensais:

[ \text{Aportes totais} = 1.000 \times 10 = R$,10.000,00 ]

Total acumulado:

[ 10.510 + 10.000 = R$,20.510,00 ]

Assim, em apenas 10 meses (até julho de 2026) você teria **R 20 510,00**, muito acima dos R 15 000 necessários, e ainda sobraria dinheiro para outros objetivos ou para aumentar a reserva.

3️⃣ Se quiser acelerar mais
Aporte mensal maior: Se você puder destinar R$ 1.500,00 por mês, a meta será atingida em cerca de 7 meses.
Investimento parcial em CDB: Combine R 1.000,00 em Tesouro Selic e R 500,00 em CDB Liquidez Diária para aproveitar a leve vantagem de rendimento do CDB.
4️⃣ Resumo rápido
Objetivo	Produto	Aporte mensal	Tempo estimado
Reserva de emergência (R$ 15 000)	Tesouro Selic	R$ 1.000,00	10 meses
Reserva de emergência (R$ 15 000)	Tesouro Selic + CDB	R$ 1.500,00	7 meses
Lembre‑se: O Tesouro Selic e o CDB Liquidez Diária são seguros e permitem resgate a qualquer momento, o que é essencial para uma reserva de emergência.

- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Desculpe, mas não tenho acesso a informações sobre a previsão do tempo. Se precisar de ajuda com algo relacionado às suas finanças, estou à disposição!
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** Desculpe, mas não tenho informações sobre um produto chamado XYZ em nosso sistema. Se quiser, posso ajudá‑lo a analisar algum dos produtos que já temos disponíveis (Tesouro Selic, CDB Liquidez Diária, LCI/LCA, etc.) ou a buscar mais detalhes sobre outros investimentos que se encaixam no seu perfil moderado. Como posso auxiliá‑lo?
- **Resultado:** [x] Correto  [ ] Incorreto

---

# Formulário de Feedback

Utilize este formulário para recolher feedback dos participantes dos testes.

| Métrica | Pergunta | Nota (1-5) |
| :--- | :--- | :--- |
| **Assertividade** | "A resposta respondeu à sua pergunta?" | 5 |
| **Segurança** | "As informações pareceram confiáveis?" | 5 |
| **Coerência** | "A linguagem foi clara e fácil de entender?" | 5 |

**Comentário aberto:** O que poderia melhorar?
Tempo de resposta
---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- Todas as interações de teste funcionou super bem

**O que pode melhorar:**
- Pode melhora a Interface caso essa solução suba para uma produção

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
