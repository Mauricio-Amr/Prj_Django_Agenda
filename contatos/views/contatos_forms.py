# type:ignore

from django.shortcuts import render, redirect
from contatos.forms import ContatoForms

# Create your views here.


def create(request):

    if request.method == 'POST':

        form = ContatoForms(data=request.POST)

        context = {
            'form': form

        }

        if form.is_valid():
            form.save()
            print('Formulario é valido')
            return redirect('contatos:create')

        return render(
            request,
            'contatos/create.html',
            context=context
        )

    context = {
        'form': ContatoForms()
    }

    return render(
        request,
        'contatos/create.html',
        context=context
    )
