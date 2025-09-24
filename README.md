# 🧠 MCP ASIMOV - Servidor \& Cliente Python 🚀

Este projeto faz parte do Curso ASIMOV e demonstra uma arquitetura MCP (Multi-Agent Communication Protocol) em Python, permitindo integração entre MCP Servers e Clients para conectar-se com APIs externas, IA (OpenAI), Wikipedia e previsão do tempo. O projeto demonstra como construir ferramentas robustas, interativas e escaláveis.

## ✨ Funcionalidades Principais

- Conexão de agentes MCP em Python (Servidor e Cliente)
- Consulta resumida à Wikipedia PT-BR
- Busca de informações Meteorológicas via OpenWeather
- Síntese de respostas usando OpenAI GPT-4o
- Execução local com SSE e Stdio

***

## 🏗️ Estrutura do Projeto

```plaintext
mcp-asimov/
├── servidor_wikipedia.py     # MCP Server para Wikipedia
├── servidor_tempo.py         # MCP Server para meteorologia
├── servidor_wikipedia_local.py # Wikipedia via stdio
├── cliente_tempo_openai.py   # Cliente MCP + OpenAI Tempo
├── cliente_wikipedia_openai.py # Cliente MCP + OpenAI Wikipedia
├── .env                      # Dados sensíveis (API Keys)
└── README.md                 # Este arquivo
```


***

## 🛠️ Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/SEU_USUARIO/mcp-asimov.git
cd mcp-asimov
```

2. **Crie e ative um ambiente virtual (recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**
```bash
pip install fastmcp wikipedia requests python-dotenv openai
```


***

## 🔑 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com suas chaves:

```env
CHAVE_API_OPENWEATHER=sua_chave_openweather
CHAVE_API_OPENAI=sua_chave_openai
```


***

## 🚦 Como Executar Localmente

### 1️⃣ Servidor MCP Wikipedia (SSE)

```bash
python servidor_wikipedia.py
```

*Disponível via SSE em `http://localhost:8000/sse`*

### 2️⃣ Servidor MCP Meteorologia

```bash
python servidor_tempo.py
```

*Transporte via stdio (stdin/stdout), integrável em ambientes MCP.*

### 3️⃣ Cliente MCP + OpenAI Tempo

```bash
python cliente_tempo_openai.py
```

*Busca previsão do tempo, sintetiza resposta amigável com OpenAI GPT.*

### 4️⃣ Cliente MCP + OpenAI Wikipedia

```bash
python cliente_wikipedia_openai.py
```

*Busca na Wikipedia e formata resposta utilizando IA generativa.*

***

## 🧩 Exemplos de Uso

### Wikipedia via Cliente

```python
cliente = Client("http://localhost:8000/sse")
resultado = await cliente.call_tool("buscar_wikipedia", arguments={"busca": "Steve Jobs"})
print(resultado)
```


### Tempo via Cliente

```python
cliente = Client("http://localhost:8000/sse")
tempo = await cliente.call_tool("buscar_tempo_atual", arguments={"local": "Rio de Janeiro"})
previsao = await cliente.call_tool("buscar_previsao_tempo", arguments={"local": "Rio de Janeiro"})
print(tempo, previsao)
```


### Integração com OpenAI

```python
cliente_openai = OpenAI(api_key=os.environ['CHAVE_API_OPENAI'])
response = cliente_openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{...}, {...}]
)
print(response.choices[0].message.content)
```


***

## 📦 Principais Dependências

- [fastmcp](https://pypi.org/project/fastmcp/) - Servidor/cliente MCP Python
- [wikipedia](https://pypi.org/project/wikipedia/) - Busca e resumo Wikipedia PT-BR
- [requests](https://pypi.org/project/requests/) - Consumo de APIs HTTP
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Gerenciamento de variáveis de ambiente
- [openai](https://pypi.org/project/openai/) - Integração com modelos GPT

***

## 💡 Observações Importantes

- O projeto é 100% em Python, podendo ser utilizado em ambientes Linux/Mac/Windows.
- Para rodar com SSE, pode ser necessário liberar portas no firewall ou ajustar configurações de rede local.
- As funções MCP implementadas podem ser facilmente adaptadas para outros agentes, redes, ou APIs externas.

***

## 🙋‍♂️ Créditos e Apoio

Este código foi idealizado durante o Curso ASIMOV. Dúvidas, sugestões, melhoramentos? Abra um issue no repositório ou contribua via PR!

***

## 🚀 Faça Fork, Contribua e **Divirta-se!** 😎


***

**Licença:** MIT

***

Em caso de dúvidas sobre os comandos, integração ou sobre algum erro específico, pergunte ou abra uma Issue! 👍

