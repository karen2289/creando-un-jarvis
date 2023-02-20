#Pyttsx3 (Fuera de línea)

import pyttsx3

engine = pyttsx3.init()
#voice_id = 'spanish-latin-am'
voice_id = 'mbrola-es1'
engine.setProperty('voice', voice_id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
string='Hola como están, les mandamos muchos saludos'
engine.say(string)
#engine.save_to_file('Hola como están','test.mp3')
engine.runAndWait()