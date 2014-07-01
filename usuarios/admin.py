from django.contrib import admin

# Register your models here.
from usuarios.models import *

admin.site.register(TokenConvite)
admin.site.register(Professor)
admin.site.register(Monitor)
admin.site.register(Aluno)
