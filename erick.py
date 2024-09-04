import speech_recognition as aa
import pyttsx3
import pywhatkit 
import datetime
import wikipedia 

listener = aa.Recognizer() 
machine = pyttsx3.init()
 
def talk(text):
    machine.say(text) 
    machine.runAndWait()

def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("listening...") 
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "erick" in instruction:
                instruction = instruction.replace("erick", " ")
                print(instruction)  
 
    except:
        pass 

    return instruction

def play_Erick():
    instruction = input_instruction()
    print(instruction) 
    if "play" in instruction:
        song = instruction.replace("play","")
        talk("playing"+song)
        pywhatkit.playonyt(song)
    elif "time" in instruction:
        time = datetime.datetime.now().strftime("%I:%M%p")
        talk("Current time"+time)
    elif "date" in instruction:
        date = datetime.datetime.now().strftime("%d /%m /%Y")
        talk("Today's date"+date) 
    elif "how are you" in instruction:
        talk("I am fine, how about you")
    elif "what is your name" in instruction:
        talk("I am Erick, What can I do for you ?")
    elif "who is" in instruction:
        human = instruction.replace("who is", "").strip()
        if human:  # Check if the name is not empty
            try:
                info = wikipedia.summary(human, 1)
                print(info)
                talk(info)
            except wikipedia.exceptions.DisambiguationError as e:
                talk("There are multiple results. Please be more specific.")
                print(e)
            except wikipedia.exceptions.PageError:
                talk("I couldn't find information on that person.")
        else:
            talk("I didn't catch the name. Please ask again.") 
    else:
        talk("Please repeat the instruction.")

play_Erick()  


