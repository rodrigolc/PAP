# -*- coding: utf-8 -*-

from django.shortcuts import render
# Create your views here.
from usuarios.models import *
import time


# pagina para gerar tokens. Usada para testes. por enquanto. haha.
#/usuarios/tokens/
def tokens(request):
    if request.method == 'GET':
        return render(
            request,
            "usuarios/tokens/tokens.html",
            {
                "tokens": TokenConvite.objects.all(),
                "TokenConvite": TokenConvite
            }
        )
    elif request.method == 'POST':
        form = request.POST
        token = TokenConvite()
        token.token = "aaa" + str(time.time())
        token.tipo = form['tipo']
        token.save()

        return render(
            request,
            "usuarios/tokens/tokens.html",
            {
                "tokens": TokenConvite.objects.all(),
                "TokenConvite": TokenConvite
            }
        )


#/usuarios/usuarios/
def usuarios(request):
    return render(
        request,
        "usuarios/usuarios/usuarios.html", {
            "professores": Professor.objects.all,
            "monitores": Monitor.objects.all,
            "alunos": Aluno.objects.all,

        }
    )


#/usuarios/cadastro/
def cadastro(request):
    # GET = pagina de cadastro
    if request.method == "GET":
        if 'token' in request.GET:
            try:
                token = TokenConvite.objects.get(token=request.GET['token'])
            except Exception:
                return render(
                    request,
                    "usuarios/tokens/token_invalido.html"
                )
            else:
                if token.usado:
                    return render(
                        request,
                        "usuarios/tokens/token_invalido.html"
                    )
            return render(
                request,
                "usuarios/cadastro/cadastro.html", {
                    "token": request.GET['token'],
                }
            )

        else:
            return render(
                request,
                "usuarios/tokens/token_invalido.html"
            )
    elif request.method == "POST":
        token = request.POST['token']
        token = TokenConvite.objects.get(token=token)
        if token.tipo == TokenConvite.PROFESSOR:
            usuario = Professor()
        elif token.tipo == TokenConvite.MONITOR:
            usuario = Monitor()
        else:
            usuario = Aluno()
        user = User()
        name = request.POST['name']
        namesplit = name.split(' ', 1)
        user.username = request.POST['username']
        user.first_name = namesplit[0]
        user.last_name = namesplit[1] if namesplit[1] else ""
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.save()
        usuario.user = user
        usuario.token = token
        usuario.save()
        token.usado = True
        token.save()
        return render(
            request,
            "usuarios/cadastro/usuario_cadastrado.html",
            {
                'usuario': usuario
            }
        )
    else:
        return render(request, "erro.html")
