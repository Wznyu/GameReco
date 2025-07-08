import os
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from games.models import Game, GameRanking, Review


with open('data/games_description.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        Game.objects.create(
            name=row['name'],
            short_description=row['short_description'],
            long_description=row['long_description'],
            genres=row['genres'],
            minimum_system_requirement=row['minimum_system_requirement'],
            recommend_system_requirement=row['recommend_system_requirement'],
            release_date=row['release_date'],
            developer=row['developer'],
            publisher=row['publisher'],
            overall_player_rating=row['overall_player_rating'],
            number_of_reviews_from_purchased_people=int(row['number_of_reviews_from_purchased_people']),
            number_of_english_reviews=int(row['number_of_english_reviews']),
            link=row['link']
        )

with open('data/games_ranking.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            game = Game.objects.get(name=row['game_name'])
        except Game.DoesNotExist:
            print(f"Game not found: {row['game_name']}")
            continue
        GameRanking.objects.create(
            game=game,
            genre=row['genre'],
            rank_type=row['rank_type'],
            rank=int(row['rank'])
        )

# 3.  reviews.csv
with open('data/steam_game_reviews.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            game = Game.objects.get(name=row['game_name'])
        except Game.DoesNotExist:
            print(f"Game not found: {row['game_name']}")
            continue
        Review.objects.create(
            game=game,
            username=row['username'],
            review=row['review'],
            hours_played=float(row['hours_played']) if row['hours_played'] else 0,
            helpful=int(row['helpful']) if row['helpful'] else 0,
            funny=int(row['funny']) if row['funny'] else 0,
            recommendation=row['recommendation'].strip().lower() in ['true', '1', 'yes'],
            date=row['date']
        )

print("finish import data !")