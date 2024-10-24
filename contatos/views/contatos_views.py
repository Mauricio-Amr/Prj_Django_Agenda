from django.shortcuts import render, get_object_or_404, redirect
from contatos.models import Contato
from django.db.models import Q
# Create your views here.


def index(request):
    contatos = Contato.objects.filter(show=True).order_by('-id')[0:10]

    context = {'contatos': contatos,
               'site_title': 'Contato - ',
               }

    return render(
        request,
        'contatos/index.html',
        context=context
    )


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contatos:index')

    # print(search_value)
    contatos = Contato.objects\
        .filter(show=True)\
        .filter(
            Q(nome__icontains=search_value) |
            Q(sobrenome__icontains=search_value) |
            Q(telefone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')

    # print(contatos.query)

    context = {'contatos': contatos,
               'site_title': 'Search - ',
               }

    return render(
        request,
        'contatos/index.html',
        context=context
    )


def contatos(request, contato_id):
    # single_contact = Contato.objects.filter(pk=contato_id).first()
    single_contact = get_object_or_404(
        Contato.objects, pk=contato_id, show=True)  # type: ignore

    nome_contato = f'{single_contact.nome} {single_contact.sobrenome} '

    context = {
        'contato': single_contact,
        'site_title': nome_contato,


    }

    return render(
        request,
        'contatos/contatos.html',
        context=context
    )
