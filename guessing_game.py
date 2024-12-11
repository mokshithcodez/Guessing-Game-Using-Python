import pyttsx3
import random
import time
import keyboard
from greetings import greetings

#Check Out use.txt To Downloade requirements.txt

greetings.show()

engine = pyttsx3.init()

def speak(text) :
    engine.say(text)
    engine.runAndWait()


speak("Welcome To Guessing Game")

print("Welcome To Guessing Game")


i = 0
time.sleep(1)
speak("Guessing A Number")

#While Loop / Guessing Part
while i<6 :
    a = "/"
    time.sleep(0.7)
    
    print("Guessing",a)
    i = i+1
    
    
    
    a = "\\"
    time.sleep(0.7)
    
    i = i+1
    
    print("Guessing",a)
    
    a = "|"
    
    time.sleep(0.7)
    i = i+1
    
    
    print("Guessing",a)
    i = i+1
    i = i+1
    
    
speak("Sucessfully Guessed")
time.sleep(1)
speak("Now Try To Guess My Number")
    
x = random.randint(1,100)

while True :
    
    print("Type 404 To Exit")
    
    
    user_input = int(input("Your Guess : "))
    
    
    if user_input == x :
        print("You Guessed It Right")
        speak("You Guessed It Right")
        time.sleep(2)
        break
        
        
        
    
    elif user_input < x :
        print("Too Low")
        speak("Too Low")
        continue
        
    elif user_input > x :
        print("Too High")
        speak("Too High")
        continue
    
    
    elif user_input == 404 :
        speak("Exiting")
        break
    
    else :
        print("Please Enter Intger")
        speak("Please Enter Integer")
        continue
    
    
    