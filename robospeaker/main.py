import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1.Created by Harry")
    while True:
        x = input("Enter what do you want me to speak : ")
        if x == 'q':
            break
        command = pyttsx3.init()
        command.say(x)
        command.runAndWait()
