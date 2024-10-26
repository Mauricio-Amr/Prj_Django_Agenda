
# type: ignore
from django.urls import path

from contatos import views

app_name = 'contatos'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),

    # contato  (CRUD)
    path('contato/<int:contato_id>/detalhe/', views.contatos, name='contatos'),
    path('contato/create/', views.create, name='create'),



]
