#our main file.+

import speech_recognition as sr

#cria um reconhecedor
r = sr.Recognizer()

#abri o mic para capitura
with sr.Microphone() as source:
    audio = r.listen(source) # define o mic de captura
    
    print(r.recognize_google(audio))
