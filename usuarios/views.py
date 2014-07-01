# -*- coding: utf-8 -*-

from django.shortcuts import render
# Create your views here.


#pagina para gerar tokens. Usada para testes.
def token_page(request):
    if request.method:
        pass
    return render(request,"usuarios/token_page.html")
