# Integración con Gemini API - Predictor de Cáncer de Mama

## 🚀 Configuración de la API de Gemini

### 1. Obtener API Key
1. Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Inicia sesión con tu cuenta de Google
3. Crea una nueva API key
4. Copia la clave generada

### 2. Configurar Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
# Configuración de la API de Gemini
GEMINI_API_KEY=tu_api_key_de_gemini_aqui

# Configuración del modelo
MODEL_NAME=gemini-1.5-flash
```

### 3. Instalar Dependencias

```bash
pip install google-generativeai python-dotenv
```

## 🔧 Características de la Integración

### ✅ Recomendaciones Personalizadas
- **Análisis contextual**: Considera el diagnóstico, probabilidades y nivel de confianza
- **Recomendaciones específicas**: Adaptadas según el resultado (benigno/maligno)
- **Enfoque médico**: Recomendaciones de estilo de vida y seguimiento profesional

### 🛡️ Seguridad Médica
- **NO automedicación**: El prompt está diseñado para evitar recomendaciones de medicamentos
- **NO tratamientos específicos**: No sugiere dosis o tratamientos farmacológicos
- **Enfoque profesional**: Siempre enfatiza la consulta con profesionales médicos

### 📋 Contenido de las Recomendaciones
- Pasos inmediatos a seguir
- Recomendaciones de estilo de vida saludable
- Importancia del seguimiento médico profesional
- Recursos de apoyo emocional disponibles

## 🎯 Prompt de Gemini

El sistema utiliza un prompt cuidadosamente diseñado que incluye:

```
IMPORTANTE: Tu respuesta debe seguir estas pautas estrictas:
1. NO recomiendes medicamentos específicos
2. NO sugieras automedicación
3. NO proporciones dosis o tratamientos farmacológicos
4. Enfócate en recomendaciones de estilo de vida, seguimiento médico y apoyo emocional
5. Siempre enfatiza la importancia de consultar con profesionales médicos
6. Mantén un tono profesional pero empático
7. Limita la respuesta a máximo 3 párrafos
8. NO sugieras remedios caseros o tratamientos alternativos no médicos
```

## 🔄 Funcionamiento

### Con API Key Configurada
- Genera recomendaciones personalizadas usando Gemini
- Considera el contexto completo del diagnóstico
- Respuestas adaptadas y profesionales

### Sin API Key
- Usa recomendaciones básicas predefinidas
- Funcionalidad completa del predictor
- Mensajes informativos sobre la configuración

## 📊 Monitoreo

El sistema muestra en consola:
- ✅ Artefactos cargados correctamente
- ✅ API de Gemini configurada correctamente (si está configurada)
- ⚠️ API de Gemini no configurada (si no está configurada)

## 🚨 Importante

- **Este sistema es una herramienta de apoyo** y no reemplaza el diagnóstico médico profesional
- **Las recomendaciones son informativas** y siempre deben ser validadas por un médico
- **La API key debe mantenerse segura** y no compartirse públicamente

## 🔧 Solución de Problemas

### Error: "API key not found"
- Verifica que el archivo `.env` esté en la raíz del proyecto
- Confirma que la variable `GEMINI_API_KEY` esté correctamente configurada
- Reinicia la aplicación después de configurar la API key

### Error: "Quota exceeded"
- Verifica tu cuota de uso en Google AI Studio
- Considera actualizar tu plan si es necesario

### Recomendaciones básicas en lugar de personalizadas
- Verifica la configuración de la API key
- Revisa los logs de la aplicación para errores específicos 