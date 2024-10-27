
from django import forms

from django.core.exceptions import ValidationError
from . import models
# Create your forms here.


class ContatoForms(forms.ModelForm):
    class Meta:
        model = models.Contato

        fields = (
            'nome',
            'sobrenome',
            'telefone',
            'email',
            'descricao',
            'categoria',
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome')
        sobrenome = cleaned_data.get('sobrenome')

        # self.add_error(
        #     'nome',
        #     ValidationError(
        #         'messagem de erro',
        if nome == sobrenome:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo nome',
                code='invalid'
            )

        #     )
        # )

        # self.add_error(
        #     None,
        #     ValidationError(
        #         'messagem de erro',
        #         code='invalid',
        #     )
        # )

            self.add_error('nome', msg)
            self.add_error('sobrenome', msg)
        return super().clean()

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')

        if nome == 'ABC':
            self.add_error(
                'nome',
                ValidationError(
                    'veio do add error',
                    code='invalid'
                )
            )
        return nome
