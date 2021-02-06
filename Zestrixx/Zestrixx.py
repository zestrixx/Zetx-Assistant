import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import pyaudio
import wikipedia
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak('good morning zestrixx')
    elif hour >=12 and hour<18:
        speak('good afternoon zestrixx')
    else:
        speak('good evening zestrixx')
    speak('You need me zes?')

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='en-in')
        print('You asked for:',query)
    except Exception as e:
        print('Sorry, i did not understand, say that again...')
        speak('Sorry, i did not understand, say that again...')
        return 'None'
    return query

if __name__ == '__main__':
    wish_me()
    while True:
        query = take_command().lower()

        if 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open('youtube.com')

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            song_items =len(songs)
            rand = random.randint(0, song_items)
            print(rand)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[rand]))

        elif 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentence=2)
            speak('according to wikipedia,')
            speak(results)

        elif 'stackoverflow' in query:
            speak('opening youtube')
            webbrowser.open('youtube.com')

        elif 'vs code' in query:
            speak('opening youtube')
            webbrowser.open('youtube.com')

        elif 'pycharm' in query:
            speak('opening youtube')
            webbrowser.open('youtube.com')

        elif 'brave browser' in query:
            speak('opening youtube')
            webbrowser.open('youtube.com')

# wish_me()