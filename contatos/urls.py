from django.urls import path

from contatos import views

app_name = 'contatos'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contato_id>/', views.contatos, name='contatos'),  # type: ignore
]
