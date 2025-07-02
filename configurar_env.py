import os

print("=== CONFIGURADOR DE ARCHIVO .env ===")
print()

# Verificar si ya existe el archivo .env
if os.path.exists('.env'):
    print("📁 Archivo .env encontrado")
    with open('.env', 'r') as f:
        content = f.read().strip()
        if content:
            print("⚠️  El archivo .env ya tiene contenido:")
            print(content)
            print()
            respuesta = input("¿Quieres sobrescribir el contenido? (s/n): ").lower()
            if respuesta != 's':
                print("Operación cancelada.")
                exit()
        else:
            print("📝 El archivo .env está vacío")
else:
    print("📝 Creando archivo .env...")

print()
print("🔑 INGRESA TU API KEY DE GEMINI")
print("1. Ve a: https://makersuite.google.com/app/apikey")
print("2. Copia tu API key")
print("3. Pégalo aquí:")
print()

api_key = input("API Key: ").strip()

if not api_key:
    print("❌ No se ingresó ninguna API key")
    exit()

# Crear el contenido del archivo .env
env_content = f"""# Configuración de la API de Gemini
GEMINI_API_KEY={api_key}

# Configuración de Flask
SECRET_KEY=mi_clave_secreta_super_segura_2024
DEBUG=True

# Configuración del modelo
MODEL_NAME=gemini-1.5-flash
"""

# Escribir el archivo
try:
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print()
    print("✅ Archivo .env configurado correctamente!")
    print(f"   API Key guardada: {api_key[:10]}...")
    print()
    print("🔄 Ahora reinicia la aplicación para activar Gemini API")
    print("   Ejecuta: python prueba.py")
    
except Exception as e:
    print(f"❌ Error al escribir el archivo: {e}") 