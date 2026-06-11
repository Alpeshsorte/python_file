from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('ragister/', views.ragister, name='ragister'),
    path('login/', views.login, name='home'),
    path('logout/', views.logout, name='home')
]