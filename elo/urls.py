from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success_game/', views.succ_game, name='success_game'),
    path('ind_player/<str:player_name>/', views.player_view, name='ind_player')

]
