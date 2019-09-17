from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('dashboard/', views.dashboard, name='dashboard'),
  path('accounts/signup/', views.signup, name='signup'),
  path('dashboard/create/', views.create_team, name='create_team'),
  path('dashboard/add_team/', views.add_team, name='add_team'),
  path('dashboard/<int:team_id>/team_detail/', views.team_detail, name='team_detail'),
  path('dashboard/<int:team_id>/add_player/<int:player_id>/',views.add_player, name='add_player'),
  path('dashboard/<int:team_id>/drop_player/<int:player_id>/',views.drop_player, name='drop_player'),
  path('dashboard/simulate_day/', views.simulate_day, name='simulate_day'),
]

