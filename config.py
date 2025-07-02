import os
from dotenv import load_dotenv

# Cargar variables de entorno desde archivo .env
load_dotenv()

class Config:
    """Configuración de la aplicación"""
    
    # API Key de Gemini (obtener de https://makersuite.google.com/app/apikey)
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
    
    # Configuración del modelo
    MODEL_NAME = 'gemini-1.5-flash'
    
    # Configuración de recomendaciones
    MAX_RECOMMENDATION_LENGTH = 500  # caracteres máximos para recomendaciones
    
    @staticmethod
    def is_gemini_available():
        """Verifica si la API de Gemini está disponible"""
        return bool(Config.GEMINI_API_KEY) 