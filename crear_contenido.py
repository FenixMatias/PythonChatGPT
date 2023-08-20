import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def crear_contenido(tema, tokens, temperatura, modelo="text-davinci-002"):

    prompt = f"Por favor escribe un artículo corto sobre el tema: {tema}\n\n"
    respuesta = openai.Completion.create(
        engine = modelo,
        prompt = prompt,
        n = 1,
        max_tokens = tokens,
        temperature = temperatura
    )

    return respuesta.choices[0].text.strip()

def resumir_texto(texto, tokens, temperatura, modelo="gpt-3.5-turbo"):

    prompt = f"Por favor resume el siguiente texto en español: {texto}\n\n"
    content = f"{prompt}, max_tokens={tokens}"
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": content}],
        temperature=temperatura
    )

    return respuesta.choices[0].message.content

tema_original = input("Pega aquí el artículo que quieres resumir: ").rstrip("\n")
tokens = int(input("Cuantos tokens máximos tendrá tu resumen: "))
temperatura = int(input("Del 1 al 10, qué tan creativo quieres que sea tu resumen?: ")) / 10
resumen = resumir_texto(tema_original, tokens, temperatura)
print("resumen", resumen)
