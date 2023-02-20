import pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")[0]
engine.setProperty('voice', voices)
text = 'Nos espera una gran semana, se vienen cosas nuevas'
engine.save_to_file(text, 'audio.mp3')
engine.runAndWait() # Donot forget to add this line

#Para poder reproducirlo, es opcional. Tambien se puede reproducir manualmente
import pyglet
music = pyglet.resource.media('audio.mp3')
music.play()
pyglet.app.run()