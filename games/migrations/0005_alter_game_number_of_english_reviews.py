# Generated by Django 5.2.4 on 2025-07-08 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_alter_game_number_of_english_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='number_of_english_reviews',
            field=models.IntegerField(default=0),
        ),
    ]
