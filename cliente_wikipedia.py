import os
import asyncio
from fastmcp import Client
from openai import OpenAI
import dotenv

caminho_servidor = "http://localhost:8000/sse"
cliente = Client(caminho_servidor)

async def testar_servidor(cliente, busca):
    dotenv.load_dotenv()
    api_key = os.environ['CHAVE_API_OPENAI']
    async with cliente:
        argumentos = {"busca": busca}
        resultado = await cliente.call_tool("buscar_wikipedia", arguments=argumentos)
        print(resultado)
        mensagem_sistema = f"""
        Você é um bot útil que faz buscas na Wikipedia. O usuário buscou pelo seguinte tema: {busca}.
        Para esta busca, você recebeu a seguinte resposta {resultado}.
        Com base nesse conteúdo, formate uma resposta amigável ao usuário."""

        cliente_openai = OpenAI(api_key=api_key)
        response = cliente_openai.response.create(
            model="gpt-4o-mini",
            instructions=mensagem_sistema,
            input="Pode me falar mais sobre este assunto?",
            )
        print(response.output_text)


if __name__ == "__main__":
    asyncio.run(testar_servidor(
        cliente=cliente,
        busca='Steve Jobs')
        )