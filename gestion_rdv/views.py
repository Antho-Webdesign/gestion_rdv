from django.shortcuts import render, get_object_or_404
from .models import RendezVous


def liste_rendezvous(request):
    rendezvous = RendezVous.objects.all()
    context = {
        'rendezvous': rendezvous,
    }
    return render(request, 'liste_rendez-vous.html', context)


def detail_rendezvous(request, slug):
    rendezvous = get_object_or_404(RendezVous, slug=slug)
    return render(request, 'detail_rendezvous.html', {'rdv': rendezvous})
