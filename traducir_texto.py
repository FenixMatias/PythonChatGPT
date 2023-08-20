import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def traducir_texto(texto, idioma):

    prompt = f"Traduce el texto {texto} al idioma {idioma}."
    content = f"{prompt}, max_tokens={50}, temperature={0.5}"
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": content}]
    )

    return respuesta.choices[0].message.content

texto = input("Escribe el texto que quieres traducir: ").rstrip("\n")
idioma = input("A que idioma lo quieres traducir: ")
traduccion = traducir_texto(texto, idioma)

print('traduccion', traduccion)
