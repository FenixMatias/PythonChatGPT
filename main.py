import os
import openai
import spacy
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

#modelos = openai.Model.list()

modelo = "text-davinci-002"
prompt = "Cuntame una historia breve sobre un viaje a japon"

respuesta = openai.Completion.create(
    engine = modelo,
    prompt = prompt,
    n = 1, #Cantidad de respuestas
    #temperature = 1, #Precision de la respuesta
    max_tokens = 100
)

texto_generado = respuesta.choices[0].text.strip()
print(texto_generado)

#Recorremos la cantidad de respuestas
''' for i, opcion in enumerate(respuesta.choices):

    #texto_generado = opcion.text.strip()
    #print(f"Respuesta {i + 1}: {texto_generado}\n") '''

print("***")

#Analisis de respuestas spacy
modelo_spacy = spacy.load("es_core_news_md")
analisis = modelo_spacy(texto_generado)

''' for token in analisis:
    #token.pos_
    print(token.text, token.dep_, token.head.text) '''

''' for entidad in analisis.ents:

    print(entidad.text, entidad.label_) '''

ubicacion = None

for entidad in analisis.ents:

    if entidad.label_ == "LOC":

        ubicacion = entidad
        break

if ubicacion:

    prompt_entidad = f"Dime mas acerca de {ubicacion}"
    respuesta_entidad = openai.Completion.create(
        engine = modelo,
        prompt = prompt_entidad,
        n = 1,
        max_tokens = 100
    )
    print(respuesta_entidad.choices[0].text.strip())





