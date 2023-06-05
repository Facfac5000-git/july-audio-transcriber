# july-audio-transcriber
Utilización de OpenAi SpeechToText para transcribir audio desde archivos mp3.

Para utilizar este módulo se necesitan un par de preparaciones previas:

1. Se requiere tener en el ordenador instalado python (Buscar la documentación al momento de preparar el repo)
2. Se recomienda una vez hecho esto, crear un entorno virtual en el directorio donde se descargara este archivo, utilizando: python -m venv audio-transcriber
3. Para activar el entorno virtual, se utilizan diferentes comandos de acuerdo al sistema operativo. En este readme consideraremos Windows y MacOS: MAC: source audio-transcriber/bin/activate - Windows: audio-transcriber\Scripts\activate.bat
4. Se debe instalar la librería de OpenAi en el entorno virtual: python -m pip install openai
5. NOTA: Cuando se termine de utilizar el script se debe desactivar el entorno virtual con: deactivate
6. Se debe generar una key de open-ai y modificarla en el código
7. Finalmente, el archivo se puede correr finalmente con: python ./main.py
