from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password'),
        ]

        # Create activities
        Activity.objects.create(user='ironman', activity_type='run', duration=30)
        Activity.objects.create(user='spiderman', activity_type='cycle', duration=45)
        Activity.objects.create(user='batman', activity_type='swim', duration=60)
        Activity.objects.create(user='superman', activity_type='run', duration=50)

        # Create leaderboard
        Leaderboard.objects.create(user='ironman', points=100)
        Leaderboard.objects.create(user='spiderman', points=80)
        Leaderboard.objects.create(user='batman', points=90)
        Leaderboard.objects.create(user='superman', points=95)

        # Create workouts
        Workout.objects.create(name='Full Body', description='A full body workout')
        Workout.objects.create(name='Cardio Blast', description='High intensity cardio')


        # Create unique index on email using pymongo
        from pymongo import MongoClient
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        db['users'].create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
