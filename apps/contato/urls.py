from django.urls import path

from apps.contato.views import index, form, editar, remover

urlpatterns = [
    path('', index, name='index'),
    path('form', form, name='form'),
    path('editar/<int:id>', editar, name='editar'),
    path('remover/<int:id>', remover, name='remover'),
]
