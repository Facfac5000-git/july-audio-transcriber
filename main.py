import openai

# Configurar la API de OpenAI
openai.api_key = 'tu-open-ai-key'

# Ejecutar la transcripción y obtener la respuesta de OpenAI
print('Hola July! Dame un ratito, ahí traduzco tu texto :3')

mp3_file = "./audio-input.mp3"
open_ai_audio_file = open(mp3_file, "rb")
open_ai_transcribed_text = openai.Audio.transcribe('whisper-1', open_ai_audio_file)

print("Tu audio transcripto es:")
print(open_ai_transcribed_text.text)
