# Generated by Django 5.1.2 on 2024-10-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='image',
            field=models.ImageField(blank=True, upload_to='imagem/%Y/%m'),
        ),
        migrations.AddField(
            model_name='contato',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
