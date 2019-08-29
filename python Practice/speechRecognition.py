import speech_recognition as sr
import random
r = sr.Recognizer()
greetings = ["Hello there", "Hi", "What's up", "Yes?"]

with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio).lower()
        print("You said:", text)
        print("To which I respond:")
        if text.find('hello') != -1 or text.find('hey') != -1 or text.find('hi') != -1 or text.find('what\'s up') != -1:
            print(random.choice(greetings))
        else:
            print('Rude. Greet me.')
    except Exception as e:
        print("Sorry, I didn't catch that")
        print(e)