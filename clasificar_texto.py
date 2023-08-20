import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def clasificar_texto(texto):

    categorias = [
        "Arte",
        "Ciencia",
        "Deportes",
        "Educación",
        "Entretenimiento",
        "Medio Ambiente",
        "Politica",
        "Salud",
        "Tecnología"
    ]

    prompt = f"Por favor, clasifica el siguiente: '{texto}' en unas de estas categorías: {','.join(categorias)}. La categoria es: "
    content = f"{prompt}, max_tokens={50}, temperature={0.5}"
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": content}]
    )

    return respuesta.choices[0].message.content

texto_clasificar = input("Ingrese un texto: ").rstrip("\n")
clasificacion = clasificar_texto(texto_clasificar)
print('clasificacion', clasificacion)