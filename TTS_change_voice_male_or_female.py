import pyttsx3 # useing for speak to robo

speak = pyttsx3.init()
voice = speak.getProperty('voices') # getting in built voices from the system 
speak.setProperty('rate',150) # talking speed of the robo
def robo(message):
    speak.say(message)
    speak.runAndWait()

voice_type= input("which voice type you want male or female ? : ")
if(voice_type =="female"):
    speak.setProperty('voice',voice[1].id) # seting the female voice
    

while True: # aking question again and 
    text_message = input("type here : ")
    if (text_message=="exit"):
        robo("ok i am leaving")
        break
    robo(text_message)




































    



