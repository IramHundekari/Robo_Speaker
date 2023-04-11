# import os
import pyttsx3

text_speech = pyttsx3.init()


if __name__ == '__main__':
    print("Welcome to Robo Speaker......")
    print("Please Enter 'quit' to end the conversation")
    while True:
        x=input("Please Enter what you want me to speak :\n")
        byetxt="Nice to talk to you! Bye..."
        if x=="quit":
            text_speech.say(byetxt)
            text_speech.runAndWait()
            break
        text_speech.say(x)
        text_speech.runAndWait()

        # os.system(command)
