from dotenv import load_dotenv
from mirascope import llm

load_dotenv()

@llm.call(model="google/gemini-flash-latest", temperature=0.7)
def saludar(texto: str) -> str:
    return f"Responde a: {texto}"

if __name__ == "__main__":
    respuesta = saludar("Hola, ¿cómo estás?")
    print(respuesta.content)
