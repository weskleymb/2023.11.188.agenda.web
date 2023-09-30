from django.urls import path

from apps.contato.views import index, form

urlpatterns = [
    path('', index, name='index'),
    path('form', form, name='form'),
]
