# Proyecto de API con LlamaIndex y Gemini

Este proyecto es una API construida con **FastAPI** que utiliza **LlamaIndex** para indexar documentos y permite realizar consultas sobre ellos utilizando modelos de lenguaje de **Gemini** y **HuggingFace**.

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Endpoints](#endpoints)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Requisitos

- Python 3.10 o superior
- Verifica las dependencias en el archivo `requirements.txt`.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/IvanPonzio/llamaindex-api.git
    cd llamaindex-api
    ```

2. Crea un entorno virtual (opcional pero recomendado):
    ```bash
    python3 -m venv env
    source env/bin/activate  # En Linux o Mac
    env\Scripts\activate     # En Windows
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Asegúrate de tener los modelos necesarios en el directorio correcto.
2. Ejecuta la aplicación:
    ```bash
    python -m app.main
    ```
3. La API estará disponible en `http://127.0.0.1:8000/docs`, donde podrás ver la documentación interactiva y probar los endpoints.

## Endpoints

### Consultar documentos

- **URL:** `/query`
- **Método:** `GET`
- **Parámetros:**
    - `q`: La pregunta que deseas realizar (tipo: string).
- **Ejemplo de uso:**
    ```http
    GET /query?q=¿Qué es LlamaIndex?
    ```

- **Respuesta:**
    ```json
    {
        "response": "Respuesta basada en los documentos disponibles."
    }
    ```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.
