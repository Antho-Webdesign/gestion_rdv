import contextlib
from django.shortcuts import render
from .models import Task
import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime


def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/task_list.html', context)


listener = sr.Recognizer()
engine = ttx.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', 'french')


def parler(text):
    engine.say(text)
    engine.runAndWait()


def ecouter(request):
    with contextlib.suppress(Exception):
        with sr.Microphone() as source:
            print("parlez maintenant")
            voix = listener.listen(source)
            command = listener.recognize_google(voix, language='fr-FR')
            command.lower()
    return render(request, 'voice_assistant.html', command)


def lancer_assistant(request):
    command = ecouter(request)
    print(command)
    if 'mets la chanson de' in command:
        chanteur = command.replace('mets la chanson de', '')
        print(chanteur)
        pywhatkit.playonyt(chanteur)
    elif 'heure' in command:
        heure = datetime.datetime.now().strftime('%H:%M')
        parler(f'il est{heure}')
    elif 'Bonjour' in command:
        parler('bonjour,ca va?')
    else:
        print('je ne comprends pas')

def voice_assistant(request):
    if request.method == 'POST':
        command = ecouter(request)
        print(command)
        if 'mets la chanson de' in command:
            chanteur = command.replace('mets la chanson de', '')
            print(chanteur)
            pywhatkit.playonyt(chanteur)
            response = f"J'ai joué la chanson de {chanteur} sur YouTube"
        elif 'heure' in command:
            heure = datetime.datetime.now().strftime('%H:%M')
            response = f'il est {heure}'
        elif 'Bonjour' in command:
            response = 'bonjour, ça va ?'
        else:
            response = 'Je ne comprends pas'

        context = {'response': response}
        return render(request, 'voice_assistant.html', context)

    return render(request, 'voice_assistant.html')
