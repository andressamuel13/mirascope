from dotenv import load_dotenv
from mirascope import llm

load_dotenv()
@llm.call("google/gemini-2.5-flash")
def enviar(prompt: str) -> str:
    return prompt

prompts = [
    "hola como estas?",
    "dime cual es la capital de japon",
    "que es la inteligencia artificial?"
]
try:
    print("modelo conectado correctamente")
    for prompt in prompts:
        respuesta = enviar(prompt)
        print(f"prompt: {prompt}\nrespuesta: {respuesta.text()}\n")  
except Exception as e:
    print("error de conexion con el modelo:", e)

