from django.shortcuts import render
from django.views.generic import DetailView
from .models import Etudiant

def acceuil(request):
    return render(request, 'pages/acceuil.html')

def etudiant(request):
    etudiant = Etudiant.objects.all()
    return render(request, 'pages/etudiant.html',{'etudiant':etudiant})

def voiretudiant(request):
    voir = Etudiant.objects.get(pk=id)
    return render(request, 'pages/voiretudiant.html', {'voir':voir})

class VoirEtudiant(DetailView):
    model = Etudiant
    template_name ="pages/voiretudiant.html"
