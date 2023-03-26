from django.urls import path
from .views import liste_rendezvous, detail_rendezvous

urlpatterns = [
    path('', liste_rendezvous, name='liste_rendezvous'),
    path('rendezvous/<slug:slug>/', detail_rendezvous, name='detail')

]
