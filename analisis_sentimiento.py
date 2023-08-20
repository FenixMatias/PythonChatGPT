import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def analizar_sentimiento(texto):

    prompt = f"Por favor, analiza el sentimiento predominante en el siguiente texto: '{texto}'. El sentimiento es :\n\n"
    content = f"{prompt}, max_tokens={100}, temperature={0.5}"
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": content}]
    )

    return respuesta.choices[0].message.content

texto_analisis = input("Ingresa un texto: ").rstrip("\n")
sentimiento = analizar_sentimiento(texto_analisis)
print('sentimiento', sentimiento)