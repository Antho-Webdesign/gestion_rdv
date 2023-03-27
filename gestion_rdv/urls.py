from django.urls import path

from notification.views import send_notification, list_notification
from tasks.views import task_list, voice_assistant
from .views import liste_rendezvous, detail_rendezvous

urlpatterns = [
    path('', liste_rendezvous, name='liste_rendezvous'),
    path('rendezvous/<slug:slug>/', detail_rendezvous, name='detail'),

    path('tasks/', task_list, name='tasks'),
    path('send-notification/', send_notification, name='send_notification'),

    path('list-notification/', list_notification, name='list_notification'),

    path('voice/', voice_assistant, name="voice"),
]
