import os

print("=== AGREGAR API KEY A .env ===")
print()

# Verificar si el archivo .env existe
if not os.path.exists('.env'):
    print("❌ Archivo .env no encontrado")
    print("Creando archivo .env...")
    
# Crear contenido del archivo .env
env_content = """# Configuración de la API de Gemini
# REEMPLAZA 'tu_api_key_aqui' con tu API key real de Gemini
GEMINI_API_KEY=tu_api_key_aqui

# Configuración del modelo
MODEL_NAME=gemini-1.5-flash
"""

# Escribir el archivo
with open('.env', 'w') as f:
    f.write(env_content)

print("✅ Archivo .env creado/actualizado")
print()
print("📝 INSTRUCCIONES:")
print("1. Abre el archivo .env con un editor de texto")
print("2. Reemplaza 'tu_api_key_aqui' con tu API key real")
print("3. Guarda el archivo")
print("4. Ejecuta: python test_gemini.py para verificar")
print()
print("🔑 Para obtener tu API key:")
print("   Ve a: https://makersuite.google.com/app/apikey")
print("   Crea una nueva API key y cópiala")
print()
print("📄 Contenido actual del archivo .env:")
print("-" * 40)
with open('.env', 'r') as f:
    print(f.read())
print("-" * 40) 