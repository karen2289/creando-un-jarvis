import speech_recognition as sr
import pyttsx3
import openai

openai.api_key = "API_KEY"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
#Configuracion del asistente masculino o femenino dependiendo el numero que se tome
engine.setProperty('voice', voices[1].id)

#Iniciamos la funcion de reconocimiento de voz y haremos que use el microfono del indice 1
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

#Crearemos 3 variables, la primera serra la conversacion donde se almacenan todas las conversaciones
#La segunda sera el nombre de usuario y la ultima la del bot.
conversation = ""
user_name = "Karen"
bot_name = "Jarvis"

#Aqui verificamos si estamos hablando o no, para eso escuchamos la entrada del microfono
while True:
    with mic as source:
        print("\n Escuchando...")
        #Sin no estamos hablando, esperara 2 segundos y nuevamente comenzara a escuchar. Este proceso continuara hasta decir algo.
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        #Si reconoce nuestra voz, imprimira que ya no escucha y guardara nuestra voz en la variable de audio.
        print("Ya no escucha")
        
        #Convertiremos nuestra voz en texto usando "pi TTS X3" hay muchas funciones usare la "recognize_google" para optener resultados mas precisos.
        #Reconociendo la funcion de Google ahora se convertira en texto automaticamente y se guardara en la variable de entrada de usuario y daremos un formato particular que se imprimira en pantalla.
        try:
            user_input = r.recognize_google(audio, language='es-ES')
        except:
            continue
        
        prompt = user_name+":"+user_input + "\n"+bot_name+":"
        conversation += prompt
        
        #Esta es la parte importante de openai "playground"
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
        
    #Obtendremos la respuesta del sistema y la almacenaremos en una cadena de respuesta.
    response_str = response["choices"][0]["text"].replace("\n", "")
    #Mostraremos el nombre del asistente que se mostrara en la pantalla de salida.
    response_str =response_str.split(
        user_name + ":" ,1)[0].split(bot_name+ ":",1)[0]

    #La cadena externa de respuesta se imprimira la salida
    conversation+= response_str +"\n"
    print(response_str)

    #Convertimos la cadena de respuesta a voz y terminamos con el programa.
    engine.say(response_str)
    engine.runAndWait()