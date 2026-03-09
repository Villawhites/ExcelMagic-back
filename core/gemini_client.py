import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    async def generate_excel_structure(self, description: str):
        prompt = f"""
        Actúa como un experto en Excel y analista de datos. 
        El usuario quiere crear un archivo Excel basado en la siguiente descripción: "{description}"
        
        Tu tarea es generar la estructura del Excel en formato JSON.
        El JSON debe incluir:
        1. "columns": Una lista de nombres de columnas.
        2. "formulas": Un diccionario opcional donde la clave es el nombre de la columna y el valor es la fórmula de Excel (usando notación de fila 2, ej: =A2*B2).
        3. "styles": Sugerencias de formato (colores de encabezado, tipos de datos).
        4. "validations": Sugerencias de validación de datos.
        
        IMPORTANTE: Devuelve ÚNICAMENTE el JSON puro, sin bloques de código ni texto adicional.
        """
        
        response = self.model.generate_content(prompt)
        try:
            # Clean response text in case it includes markdown code blocks
            text = response.text.strip()
            if text.startswith("```json"):
                text = text[7:-3].strip()
            elif text.startswith("```"):
                text = text[3:-3].strip()
            
            return json.loads(text)
        except Exception as e:
            return {
                "error": "Failed to parse LLM response",
                "raw_text": response.text,
                "exception": str(e)
            }

gemini_client = GeminiClient()
