from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Etudiant, EtudiantAdmin
from django.contrib.auth.models import User, Group

class EcesAdmin(AdminSite):
    site_header = "ECES ETUDIANT"
    index_title = "Bienvenu sur le site d'administrateur d'ECES_EDU"

admin.site = EcesAdmin(name='admin')

admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(User)
admin.site.register(Group)
