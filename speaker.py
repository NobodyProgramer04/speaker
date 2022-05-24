import pyttsx3
 
n = "yes"
while n == "yes":
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty('rate', 110)
     
    a = input("type a word:")
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    speak(a)
    n = input("Do you want restart the program?(yes/no)")
    if n == "no":
        exit()
 
