# Defines text content for app.py

instructions = """
# Truedocs

🚀 Bienvenido a Truedocs, donde revolucionamos el procesamiento de documentos.

Utilizando el poder de la Inteligencia Artificial (IA), nuestra API
está diseñada para acelerar significativamente tus flujos de trabajo de procesamiento
de documentos. Con Truedocs, puedes clasificar fácilmente una amplia gama de documentos,
desde documentos de identidad 🪪 hasta facturas de servicios públicos y mucho más.
Pero eso es sólo el comienzo.

⚡ Esta aplicación de prueba demuestra el poder y capacidades de la API de Truedocs
para aplicar inteligencia artificial sobre documentos 🖺.

Para mayor información acerca de nuestra API visita
[api.truedocs.mx/docs](https://api.truedocs.mx/docs).

Para ver el código de esta app visita
[nuestro repositorio en GitHub](https://github.com/true-docs/streamlit-demo-app).

## Instrucciones
1. Sube un documento.
1. Selecciona una operación a ejecutar.
1. Después de unos momentos, el sistema mostrará los resultados.
"""

capabilities = """
Nuestra API proporciona componentes esenciales para tus aplicaciones 🏗️,
incluidas validaciones de campo avanzadas y búsquedas inteligentes,
lo que garantiza un sistema de procesamiento más inteligente y eficiente.
Ya sea que se esté integrando con sistemas existentes o creando algo nuevo,
nuestras herramientas están diseñadas para adaptarse sin esfuerzo a tu flujo de
trabajo.
"""

intro_to_classify = """
### Clasicación de documentos

Prueba nuestro endpoint `/classify` para cargar y analizar imágenes o archivos PDF,
incluidos formatos como PNG, JPG, GIF y WEBP, para la detección automática del
tipo de documento. Esta función es particularmente útil para identificar tipos
de documentos específicos, como discernir si una imagen proviene de una factura de
servicios públicos 🏭 emitida por una empresa en particular o verificar una
identificación oficial 🪪.

Tras el procesamiento, el criterio de valoración ofrece la clasificación más
probable, acompañada de una etiqueta descriptiva y una puntuación numérica que
va de 0 a 1, lo que indica el nivel de confianza de la clasificación 📈.
"""

intro_to_extract = """
### Extracción de información

🔍 Prueba la funcionalidad de nuestro endpoint `/match`, diseñado para procesar documentos
en forma de imágenes o PDF. Simplemente carga tu documento y utilice el parámetro `identifier`
para especificar la cadena o elemento particular que está buscando dentro del documento.
El verdadero poder de esta función es su capacidad para buscar cadenas similares,
no solo coincidencias exactas, ya sea que se trate de errores tipográficos o variaciones de
palabras.

🎯 Para obtener resultados más refinados, tienes la opción de establecer un parámetro de `threshold`.
Esta puntuación actúa como una puntuación de similitud, lo que garantiza que tus mejores
resultados cumplan con una cierta similitud. Además, el parámetro `top_k` le permite definir
cuántos de los resultados de mayor clasificación desea recibir, ofreciendo flexibilidad en
tu búsqueda.

📊 Como resultado, el API te proporciona la cadena correspondiente,
cada una acompañada de su puntuación de similitud, lo que le brinda una
comprensión clara de la confiabilidad de la coincidencia.
Se proporciona una puntuación general como campo `confidence`.
"""

intro_to_validate = """
La funcionalidad del endpoint `/validate` ha sido meticulosamente diseñada para elevar
la precisión del procesamiento de tus documentos.
Esta es una herramienta para ejecutar documentos a través de un conjunto completo
de validaciones, garantizando que cada pieza de información cumpla con tus criterios
específicos.

Actualmente, cuenta con dos validaciones poderosas: `IsRecent` y `DidExpire`.

🗓️ IsRecent: Comprueba si la fecha de vencimiento de una factura o recibo se
encuentra dentro de los últimos 90 días, garantizando así que el documento sea
vigente y relevante.

🆔 DidExpire: Examina los documentos de identidad para verificar su validez.
Comprueba si documentos como las identificaciones han caducado,
lo que garantiza que solo esté trabajando con credenciales legítimas y actualizadas.
"""
