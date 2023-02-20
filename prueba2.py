#Google (Internet)
from gtts import gTTS
from io import BytesIO

tts = gTTS(text="Hola Karen, que quieres que hagamos hoy? quieres que te lea las noticias", lang='es')
tts.save("audio.mp3")
mp3_fp = BytesIO()
tts = gTTS('Hola Karen, como va tu dia', 'es')
tts.write_to_fp(mp3_fp)

#Para poder reproducir
import pyglet
music = pyglet.resource.media('audio.mp3')
music.play()
pyglet.app.run()