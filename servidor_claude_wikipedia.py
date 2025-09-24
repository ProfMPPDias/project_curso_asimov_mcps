from fastmcp import FastMCP
import wikipedia

wikipedia.set_lang("pt")

servidor_mcp = FastMCP("mcp-busca-wikipedia")

@servidor_mcp.tool()
async def buscar_wikipedia_local(busca: str) -> str:
    try:
        # Tenta buscar com auto_suggest desabilitado
        return wikipedia.summary(busca, auto_suggest=False)
    except wikipedia.exceptions.PageError:
        return "Nenhuma página encontrada para esse termo!"
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Página ambígua. Escolha entre: {', '.join(e.options[:5])}"

if __name__ == "__main__":
    servidor_mcp.run(transport="stdio")