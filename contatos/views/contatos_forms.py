from django.shortcuts import render, get_object_or_404, redirect
from contatos.models import Contato
from django.db.models import Q

from django.core.paginator import Paginator

# Create your views here.


def create(request):

    context = {

    }

    return render(
        request,
        'contatos/create.html',
        context=context
    )
