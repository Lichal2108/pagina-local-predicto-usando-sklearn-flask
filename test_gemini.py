import os
from dotenv import load_dotenv
import google.generativeai as genai

# Cargar variables de entorno
load_dotenv()

print("=== PRUEBA DE CONFIGURACIÓN GEMINI API ===")
print()

# Verificar si existe el archivo .env
if os.path.exists('.env'):
    print("✅ Archivo .env encontrado")
else:
    print("❌ Archivo .env NO encontrado")
    print("   Crea un archivo .env en la raíz del proyecto")

print()

# Verificar la API key
api_key = os.getenv('GEMINI_API_KEY', 'AIzaSyA7evjmRwUEECBNBFaOiWgfxV8GEEzfBZQ')
if api_key:
    print("✅ API Key encontrada en .env")
    print(f"   Longitud: {len(api_key)} caracteres")
    print(f"   Inicia con: {api_key[:10]}...")
else:
    print("❌ API Key NO encontrada en .env")
    print("   Asegúrate de que GEMINI_API_KEY esté en tu archivo .env")

print()

# Intentar configurar Gemini
try:
    genai.configure(api_key=api_key)  # type: ignore
    print("✅ Gemini configurado correctamente")
    
    # Probar la conexión
    model = genai.GenerativeModel('gemini-1.5-flash')  # type: ignore
    response = model.generate_content("Hola, ¿funcionas?")
    print("✅ Conexión exitosa con Gemini API")
    print(f"   Respuesta: {response.text}")
    
except Exception as e:
    print("❌ Error al conectar con Gemini API")
    print(f"   Error: {str(e)}")
    
    if "API key" in str(e).lower():
        print("   → Verifica que tu API key sea correcta")
    elif "quota" in str(e).lower():
        print("   → Verifica tu cuota de uso en Google AI Studio")
    elif "network" in str(e).lower():
        print("   → Verifica tu conexión a internet")

print()
print("=== CONTENIDO DEL ARCHIVO .env ===")
if os.path.exists('.env'):
    with open('.env', 'r') as f:
        content = f.read()
        # Ocultar la API key por seguridad
        if api_key:
            content = content.replace(api_key, "***API_KEY_OCULTA***")
        print(content)
else:
    print("Archivo .env no encontrado")

print()
print("=== INSTRUCCIONES ===")
print("1. Asegúrate de que el archivo .env esté en la raíz del proyecto")
print("2. El archivo .env debe contener: GEMINI_API_KEY=tu_api_key_aqui")
print("3. Reinicia la aplicación después de configurar el .env")
print("4. Ejecuta: python test_gemini.py para verificar") 