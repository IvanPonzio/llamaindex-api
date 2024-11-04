from fastapi import FastAPI, HTTPException
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from pydantic import BaseModel
import os

app = FastAPI()

# Configuración de LlamaIndex con el modelo LLM y embeddings
llm = Gemini(model="models/gemini-pro", api_key="AIzaSyCpcPwrzy-LnIdtRSbweol2y_ibZvA_Su0")
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# Asignación de los modelos a las configuraciones de LlamaIndex
Settings.llm_model = llm
Settings.embed_model = embed_model

# Carga e indexación de documentos en el directorio data/
data_directory = "./data"
documents = SimpleDirectoryReader(data_directory).load_data()  # Cargar documentos .txt desde el directorio
index = VectorStoreIndex.from_documents(documents)  # Crear índice a partir de los documentos
query_engine = index.as_query_engine(llm=llm)  # Crear motor de consulta utilizando el LLM

# Modelo de respuesta para estructurar la salida
class QueryResponse(BaseModel):
    response: str

# Endpoint para realizar consultas
@app.get("/query", response_model=QueryResponse, 
         description="Consulta información en documentos indexados. Proporciona una pregunta y recibe la respuesta basada en los documentos disponibles.")
async def query(q: str):
    """
    Realiza una consulta a los documentos indexados.

    - **q**: La pregunta que se desea hacer. Debe ser un string.
    
    Ejemplo: GET /query?q=¿Qué es LlamaIndex?
    """
    if not q:
        raise HTTPException(status_code=400, detail="Parámetro de consulta 'q' es obligatorio.")
    
    try:
        response = query_engine.query(q)  # Realiza la consulta en el índice
        simple_response = response.response
        
        # Manejo del caso donde no se encuentran resultados relevantes
        if not simple_response or "not mention" in simple_response:
            return QueryResponse(response="Lo siento, no encontré información sobre tu consulta. Intenta con otra pregunta.")
    except Exception as e:
        # Manejo de errores internos
        raise HTTPException(status_code=500, detail=f"Error en el procesamiento de la consulta: {str(e)}")
    
    return QueryResponse(response=simple_response)  # Devuelve la respuesta de la consulta

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)  # Ejecuta la aplicación
