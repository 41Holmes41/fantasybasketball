from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TeamForm
from .models import Player, Team, Game, Day
import random



def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    try:
        team=Team.objects.get(owner_id=request.user.id)
    except Team.DoesNotExist:
        team={}

    return render(request, 'dashboard/dashboard.html',{'team':team})

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
    myplayers = Player.objects.filter(owner=request.user)
    
    return render(request, 'dashboard/team_detail.html', {
        'team':team,
        'players':players,
        'myplayers':myplayers,
    })

def add_player(request, team_id, player_id):
    
    Team.objects.get(id=team_id).players.add(player_id)
    player = Player.objects.get(id=player_id)
    player.owner = request.user
    player.status = False
    player.save()
    return redirect('team_detail', team_id=team_id)

def drop_player(request, team_id, player_id):
    Team.objects.get(id=team_id).players.remove(player_id)
    player = Player.objects.get(id=player_id)
    player.owner=None
    player.status = True
    player.save()
    return redirect('team_detail', team_id=team_id)

def simulate_day(request):
    players=Player.objects.filter(status='False')
    day=Day.objects.get()
    day.day_counter+=1
    day.save()
    # print(players)
    for player in players:
        team=Team.objects.get(owner=player.owner)
        game=Game.objects.create()
        game.player=player
        game.owner=player.owner 
        game.day_played=day.day_counter
        game.points=round(player.point_rating * random.random() * 5) + (player.point_rating)
        # print(game.points)
        game.rebounds=round(player.rebound_rating * random.random() * 2) + (round(player.rebound_rating/2))
        game.assists=round(player.assist_rating * random.random() * 1.5) + (round(player.assist_rating/2))
        game.steals=round(player.steal_rating * random.random() * .5) + (round(random.random()*2))
        game.blocks=round(player.block_rating * random.random() * .5 + player.block_rating * random.random()*.5)
        game.turnovers=round((10-player.turnover_rating) * random.random())
        game.threepointers=round(player.threepointer_rating*random.random()+random.random())
        game.save()

        team.team_points+=game.points
        team.team_rebounds+=game.rebounds
        team.team_assists+=game.assists
        team.team_steals+=game.steals
        team.team_blocks+=game.blocks
        team.team_turnovers+=game.turnovers
        team.team_threepointers+=game.threepointers
        team.save()
    return redirect('dashboard')

def results(request):
    teams=Team.objects.all()
    games=Game.objects.all()
    day=Day.objects.get()
    days=[]
    for day in range(day.day_counter):
        days.append(day + 1)
    print(games[34].owner, teams[2].owner)



    return render(request, 'dashboard/results.html', {
        'teams':teams,
        'games':games,
        'days':days,
    })

""" def dayresults(request):
    teams=Team.objects.all()
    games=Game.objects.all()
    day=Day.objects.get()
    days=[]
    for day in range(day.day_counter):
        days.append(day + 1)
    print(days)

    return render(request, 'dashboard/results.html', {
        'teams':teams,
        'games':games,
        'days':days,
        'selected_day': day_num,
    }) """

def start_league(request):
    day = Day.objects.create()
    day.day_counter=0
    day.save()
    return redirect('dashboard')

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

