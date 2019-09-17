from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User
# Create your models here.


class Player(models.Model):
  first_name=models.CharField(max_length=50,null=True)
  last_name=models.CharField(max_length=50, null=True)
  nba_team=models.CharField(max_length=50, null=True)
  point_rating=models.IntegerField(null=True)
  rebound_rating=models.IntegerField(null=True)
  assist_rating=models.IntegerField(null=True)
  steal_rating=models.IntegerField(null=True)
  block_rating=models.IntegerField(null=True)
  turnover_rating=models.IntegerField(null=True)
  threepointer_rating=models.IntegerField(null=True)
  status=models.BooleanField(null=True) #True means player available / False Player is taken

  def __str__(self):
    return f'{self.first_name} {self.last_name}'
  
class Team(models.Model):
  players = models.ManyToManyField(Player, null=True)
  owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  team_name=models.CharField(max_length=50,null=True)
  team_points=models.IntegerField(null=True)
  team_rebounds=models.IntegerField(null=True)
  team_assists=models.IntegerField(null=True)
  team_steals=models.IntegerField(null=True)
  team_blocks=models.IntegerField(null=True)
  team_turnovers=models.IntegerField(null=True)
  team_threepointers=models.IntegerField(null=True)
  owner_points=models.TextField(max_length=250, null=True)
  rank=models.IntegerField(null=True)

  def get_absolute_url(self):
    return reverse('team_detail', kwargs={'team_id':self.id})

class Game(models.Model):
  player=models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
  points=models.IntegerField(null=True)
  rebounds=models.IntegerField(null=True)
  assists=models.IntegerField(null=True)
  steals=models.IntegerField(null=True)
  blocks=models.IntegerField(null=True)
  turnovers=models.IntegerField(null=True)
  threepointers=models.IntegerField(null=True)
  team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
  day=models.IntegerField(null=True)

  def __str__(self):
    return f"{self.player_id}'s game"

  