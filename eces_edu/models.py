from django.db import models
from django.contrib import admin

class Etudiant(models.Model):
    photo = models.ImageField()
    matricule = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=100)
    niveau = models.CharField(max_length=100)
    filiere = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)

    def __str__(self):
        return self.nom.title()

class EtudiantAdmin(admin.ModelAdmin):
    list_display=('nom', 'prenom', 'niveau', 'filiere', 'photo')
