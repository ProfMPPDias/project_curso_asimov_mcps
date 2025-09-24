import os
import asyncio
from fastmcp import Client
from openai import OpenAI
import dotenv

caminho_servidor = "http://localhost:8000/sse"
cliente = Client(caminho_servidor)

async def testar_servidor(cliente, local):
    dotenv.load_dotenv()
    api_key = os.environ['CHAVE_API_OPENAI']

    async with cliente:
        argumentos = {"local": local}
        tempo_atual = await cliente.call_tool("buscar_tempo_atual", arguments=argumentos)
        previsao_tempo = await cliente.call_tool("buscar_previsao_tempo", arguments=argumentos)

        mensagem_sistema = f"""
        Você é um bot que faz buscas de previsão do tempo e sintetiza as respostas.
        O usuário buscou pela previsão no seguinte local: {local}.
        Para esta busca, você recebeu as seguintes previsões: {previsao_tempo}.
        Além disso, o tempo atual é {tempo_atual}.
        Com base nessas informações, responda de forma amigável ao usuário.
        """

        cliente_openai = OpenAI(api_key=api_key) 
        response = cliente_openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": mensagem_sistema},
                {"role": "user", "content": "Qual a previsão de tempo no local indicado?"}
            ]
        )
        print(response.choices[0].message.content)

if __name__ == "__main__":
    asyncio.run(testar_servidor(
        cliente=cliente,
        local='Rio de Janeiro'
    ))