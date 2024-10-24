from django.urls import path

from contatos import views

app_name = 'contatos'

urlpatterns = [
    path('<int:contato_id>/', views.contatos, name='contatos'),  # type: ignore
    path('search/', views.search, name='search'),  # type: ignore
    path('', views.index, name='index'),
]
