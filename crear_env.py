import os

print("=== CREAR ARCHIVO .env CON CODIFICACIÓN CORRECTA ===")
print()

# Crear contenido del archivo .env con codificación UTF-8
env_content = """# Configuracion de la API de Gemini
# REEMPLAZA 'tu_api_key_aqui' con tu API key real de Gemini
GEMINI_API_KEY=tu_api_key_aqui

# Configuracion del modelo
MODEL_NAME=gemini-1.5-flash
"""

# Escribir el archivo con codificación UTF-8
try:
    with open('.env', 'w', encoding='utf-8') as f:
        f.write(env_content)
    
    print("✅ Archivo .env creado correctamente con codificación UTF-8")
    print()
    print("📝 INSTRUCCIONES:")
    print("1. Abre el archivo .env con un editor de texto (Notepad, VS Code)")
    print("2. Reemplaza 'tu_api_key_aqui' con tu API key real")
    print("3. Guarda el archivo")
    print("4. Ejecuta: python test_gemini.py para verificar")
    print()
    print("🔑 Para obtener tu API key:")
    print("   Ve a: https://makersuite.google.com/app/apikey")
    print("   Crea una nueva API key y copiala")
    print()
    print("📄 Contenido del archivo .env:")
    print("-" * 40)
    print(env_content)
    print("-" * 40)
    
except Exception as e:
    print(f"❌ Error al crear el archivo: {e}") 