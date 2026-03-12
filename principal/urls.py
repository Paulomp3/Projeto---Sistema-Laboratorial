from django.urls import path
from principal import views

urlpatterns = [
    path('', views.login, name='login'),
]
