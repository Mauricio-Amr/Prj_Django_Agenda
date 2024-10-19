import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'Prj_Agenda.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from contatos.models import Categoria, Contato

    # Contato.objects.all().delete()
    # Categoria.objects.all().delete()

    fake = faker.Faker('pt_BR')
    categoria = ['Amigos', 'Família', 'Conhecidos']

    django_categories = [Categoria(nome=nome) for nome in categoria]

    for categoria in django_categories:
        categoria.save()

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        nome, sobrenome = profile['name'].split(' ', 1)  # type: ignore
        telefone = fake.phone_number()
        data_criacao: datetime = fake.date_this_year()  # type: ignore
        descricao = fake.text(max_nb_chars=100)
        categoria = choice(django_categories)

        django_contacts.append(
            Contato(
                nome=nome,
                sobrenome=sobrenome,
                telefone=telefone,
                email=email,
                data_criacao=data_criacao,
                descricao=descricao,
                categoria=categoria,
            )
        )

    if len(django_contacts) > 0:
        Contato.objects.bulk_create(django_contacts)
