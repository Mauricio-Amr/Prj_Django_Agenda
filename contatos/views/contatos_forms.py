# type:ignore

from typing import Any, Dict
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from contatos.models import Contato
from django.db.models import Q

from django.core.paginator import Paginator
from django.core.exceptions import ValidationError

# Create your views here.


class ContatoForms(forms.ModelForm):
    class Meta:
        model = Contato
        fields = (
            'nome',
            'sobrenome',
            'telefone',
        )

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            'nome',
            ValidationError(
                'messagem de erro',
                code='invalid',
            )
        )

        self.add_error(
            None,
            ValidationError(
                'messagem de erro',
                code='invalid',
            )
        )
        return super().clean()


def create(request):

    if request.method == 'POST':
        context = {
            'form': ContatoForms(data=request.POST)

        }

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
