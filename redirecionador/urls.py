from django.urls import path

from . import views

app_name = 'redirecionador'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:url_curta>/', views.redireciona_usuario, name='redireciona_usuario'),
]