# -*- coding: utf-8 -*-

from django.shortcuts import render
# Create your views here.
from usuarios.models import *

#pagina para gerar tokens. Usada para testes.
def tokens(request):
    if request.method == 'POST':
        form = request.POST
        token = TokenConvite()
        token.token="aaa" + now()
        token.tipo = form['tipo']
        token.save()

	for tok in TokenConvite.objects.all():
		print tok.str()

    return render(request,"usuarios/tokens.html",{"TokenConvite":TokenConvite})


def usuario(request):
    
    return render(request,"usuarios/tokens.html",{
    	"TokenConvite":TokenConvite,

    	})
 