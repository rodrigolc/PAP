# -*- coding: utf-8 -*-
from django.shortcuts import render
from pages.models import *
from usuarios.models import *

# Create your views here.


def get_usuario(page, user):
    pagina = Pagina.objects.get(link=page)

    try:
        professor = Professor.objects.get(user=user, pagina=pagina)
    except Exception:
        pass
    else:
        return professor

    try:
        monitor = Monitor.objects.get(user=user, pagina=pagina)
    except Exception:
        pass
    else:
        return monitor

    try:
        aluno = Aluno.objects.get(user=user, pagina=pagina)
    except Exception:
        raise Exception("user nao encontrado")
    else:
        return aluno

# acha a aba certa, gera a pagina
# view principal do sistema. basicamente tudo aqui é feito por aqui


def aba(request, pagina, aba):
    try:
        pagina = Pagina.objects.get(link=pagina)
        aba_model = Aba.objects.get(link=aba, pagina=pagina)
    except Exception:
        return erro(request)
    else:
        pass
    finally:
        pass

    template_base = pagina.layout
    widgets = aba_model.widgets.all()

    # carregar abas do nav
    autorizacao = 0
    if request.user.is_authenticated() and not request.user.is_staff:
        usuario = get_usuario(pagina, request.user)
        autorizacao = usuario.token.tipo
    elif request.user.is_authenticated():
        autorizacao = 3
    if int(aba_model.acesso) > autorizacao:
        return erro(request)

    # filtra abas que o usuario nao tem acesso.
    abas = Aba.objects.filter(acesso__lte=autorizacao)

    # carregar widgets da aba
    for widget in widgets:
        widget.txt = widget.parse(request, {"widget": widget})
    # retornar aba

    return render(request, "pages/aba.html", {
        "titulo": pagina.titulo,
        "sub_titulo": aba_model.titulo,
        "widgets": widgets,
        "base": "pages/layouts/" + template_base + ".html",
        "aba_ativa": aba_model,
        "abas": abas,
        "request": request,
        "autorizacao": autorizacao,
        "pagina": pagina
    })


# Pagina inicial
def index(request, pagina):
    # tem que achar a aba inicial,
    aba_inicial = "index"
    return aba(request, aba_inicial)


def erro(request):
    return render(request, "erro.html")
