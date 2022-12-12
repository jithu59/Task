
from django.urls import path

from bankapp import views

urlpatterns = [

    path('', views.demo, name='demo'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('submit/', views.submit, name='submit'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # AJAX
]