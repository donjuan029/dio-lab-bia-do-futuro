# Passo a passo de Execução

Esta pasta contém o código do seu agente financeiro.

## Setup do Ollama

```bash
# 1 - Instalar Ollama(ollama.com)
# 2 - Baixar um modelo leve
# 3 - Ollama pull gpt-oss
# 4 - Testar se funciona
# 5 - ollama run gpt-oss "Olá!!!!"
```

## Código Completo

Todo o código fonte está no arquivo: `app.py`.

## Como Rodar

```bash
# 1 - Instalar dependências
pip install -r requirements.txt

# 2 - Rodar a aplicação
streamlt run .\src\app.py
```

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit)
├── agente.py           # Lógica do agente
├── config.py           # Configurações (API keys, etc.)
└── requirements.txt    # Dependências
```

## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
```
