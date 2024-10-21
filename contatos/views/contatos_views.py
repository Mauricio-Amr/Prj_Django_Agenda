from django.shortcuts import render
from contatos.models import Contato

# Create your views here.


def index(request):
    contatos = Contato.objects.filter(show=True).order_by('-id')[0:10]

    context = {'contatos': contatos}

    return render(
        request,
        'contatos/index.html',
        context=context
    )


def contatos(request, contato_id):
    single_contact = Contato.objects.get(pk=contato_id)

    context = {'contato': single_contact}

    return render(
        request,
        'contatos/contatos.html',
        context=context
    )
