import contextlib
import datetime

import pyttsx3 as ttx
import pywhatkit
import speech_recognition as sr
from django.shortcuts import render
from django.views import View

from tasks.models import Task


def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/task_list.html', context)


class VoiceAssistant(View):
    listener = sr.Recognizer()
    engine = ttx.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', 'french')

    def parler(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def ecouter(self, request):
        with contextlib.suppress(Exception):
            with sr.Microphone() as source:
                print("parlez maintenant")
                voix = self.listener.listen(source)
                print(source)
                command = self.listener.recognize_google(voix, language='fr-FR')
                command = command.lower()
                return render(request, 'voice_assistant.html', {'command': command})
        return render(request, 'voice_assistant.html')

    def lancer_assistant(self, request):
        if request.method == 'POST':
            command = self.ecouter(request)
            print(command)
            if 'bonjour' in command:
                chanteur = command.replace('mets la chanson de', '')
                print(chanteur)
                pywhatkit.playonyt(chanteur)
            elif 'heure' in command:
                heure = datetime.datetime.now().strftime('%H:%M')
                return render(request, 'voice_assistant.html', {'response': f'il est {heure}'})
            elif 'Bonjour' in command:
                return render(request, 'voice_assistant.html', {'response': 'bonjour, ca va?'})
            elif 'ajoute une tache' in command:
                title = command.replace('ajoute une tache intitulee', '')
                Task.objects.create(title=title, description='', due_date=datetime.datetime.now())
                return render(request, 'voice_assistant.html', {'response': f'la tache {title} a ete ajoutee'})
            else:
                print('je ne comprends pas')
        return render(request, 'voice_assistant.html')

    def get(self, request):
        return render(request, 'voice_assistant.html')

    def post(self, request):
        return self.lancer_assistant(request)

