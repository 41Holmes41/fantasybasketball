from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TeamForm
from .models import Player, Team 

def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def create_team(request):
    team_form = TeamForm()
    return render(request, 'dashboard/team_form.html',{
        'team_form':team_form,
    })

def add_team(request):
    form = TeamForm(request.POST)
    if form.is_valid():
        new_team=form.save(commit=False)
        new_team.owner = request.user
        new_team.save()
    return redirect('team_detail', team_id=new_team.id)


def team_detail(request, team_id):
    team = Team.objects.get(id=team_id)
    players = Player.objects.all()
    
    return render(request, 'dashboard/team_detail.html', {
        'team':team,
        'players':players
    })

def add_player(request, team_id, player_id):
    
    Team.objects.get(id=team_id).players.add(player_id)
    player = Player.objects.get(id=player_id)
    player.status = False
    player.save()
    return redirect('team_detail', team_id=team_id)

def drop_player(request, team_id, player_id):
    Team.objects.get(id=team_id).players.remove(player_id)
    player = Player.objects.get(id=player_id)
    player.status = True
    player.save()
    return redirect('team_detail', team_id=team_id)

def signup(request):
    error_message=''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = 'Invalid sign up-Try Again'
    form = UserCreationForm()
    context = {'form': form, 'error_message':error_message}
    return render(request, 'registration/signup.html', context)

