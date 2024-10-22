from django.shortcuts import render, get_object_or_404
from contatos.models import Contato
from django.http import Http404
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
    # single_contact = Contato.objects.filter(pk=contato_id).first()
    single_contact = get_object_or_404(
        Contato.objects, pk=contato_id, show=True)  # type: ignore

    context = {'contato': single_contact}

    return render(
        request,
        'contatos/contatos.html',
        context=context
    )
