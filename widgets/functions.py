
from django.template.loader import render_to_string
# -*- coding: utf-8 -*-
from widgets.models import *

from usuarios.models import *
from pages.models import *
# Criar aqui as funcoes de parsing dos widgets


def default(widget):
    return render_to_string("widgets/files/widget1.html", {})


def calendario(widget, request, obj):
    return render_to_string("widgets/files/calendar.html", obj)


def notas(widget, request, obj):
    # from widgets.models import *
    boletim = Boletim.objects.get(widget=widget)

    alunos = Aluno.objects.filter(pagina=boletim.pagina).all()
    _notas = []
    for aluno in alunos:
        print aluno.user.get_full_name()
        print aluno.token.token
        ns = []
        nsum = 0.0
        for avaliacao in boletim.avaliacoes.all():
            try:
                n = avaliacao.notas.get(aluno=aluno).nota
            except Exception, e:
                print e
                n = 0.0
            finally:
                ns.append(n)
                nsum += n * avaliacao.peso
        _notas.append(
            {"nome": aluno.user.get_full_name(), "notas": ns, "media": nsum})

    obj.update(
        {
            "boletim": boletim,
            "notas": _notas,
            "widget": widget,
            "gambi": range(20)}
    )
    print _notas
    return render_to_string("widgets/files/notas.html", obj)


def textWidget(widget, request, obj):
    # from widgets.models import *
    text_widget = TextWidget.objects.get(widget=widget)
    obj.update({"widget": text_widget})
    return render_to_string("widgets/files/textWidget.html", obj)
