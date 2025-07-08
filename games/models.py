from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=255, default='unknown')
    short_description = models.TextField(default='unknown')
    long_description = models.TextField(default='unknown')
    genres = models.CharField(max_length=255, default='unknown')
    minimum_system_requirement = models.TextField(default='unknown')
    recommend_system_requirement = models.TextField(default='unknown')
    release_date = models.CharField(max_length=100, default='unknown')
    developer = models.CharField(max_length=255, default='unknown')
    publisher = models.CharField(max_length=255, default='unknown')
    overall_player_rating = models.CharField(max_length=50, default='unknown')
    number_of_reviews_from_purchased_people = models.IntegerField(default=0)
    number_of_english_reviews = models.IntegerField(default=0)
    link = models.URLField(default='unknown')

class GameRanking(models.Model):
    game_name = models.CharField(max_length=255, default='unknown')
    genre = models.CharField(max_length=100, default='unknown')
    rank_type = models.CharField(max_length=100, default='unknown')
    rank = models.IntegerField(default=0)

class Review(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)  
    username = models.CharField(max_length=100, default='unknown')
    review = models.TextField(default='unknown')
    hours_played = models.FloatField(default=0.0)
    helpful = models.IntegerField(default=0)
    funny = models.IntegerField(default=0)
    recommendation = models.BooleanField(default=False)
    date = models.CharField(max_length=100, default='unknown')