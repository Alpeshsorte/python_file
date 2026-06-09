from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('ragister/', views.ragister, name='ragister'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('quiz/', views.quiz, name="quiz" )
] 