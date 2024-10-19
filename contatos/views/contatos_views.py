from django.shortcuts import render
from contatos.models import Contato

# Create your views here.


def index(request):
    contatos = Contato.objects.all

    context = {'contatos': contatos}

    return render(
        request,
        'contatos/index.html',
        context=context
    )
