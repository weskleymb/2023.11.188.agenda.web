from django.urls import path

from apps.contato.views import index

urlpatterns = [
    path('', index, name='index'),
]
