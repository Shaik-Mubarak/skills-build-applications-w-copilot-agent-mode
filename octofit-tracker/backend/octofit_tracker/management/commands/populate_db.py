from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models


from octofit_tracker.models import Team, Activity, Leaderboard, Workout
from django.db import connections

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data



        # Drop collections directly using pymongo
        db_conn = connections['default']
        db_conn.ensure_connection()
        db = db_conn.connection.client[db_conn.settings_dict['NAME']]
        for model in [Activity, Leaderboard, Workout, Team, User]:
            collection_name = model._meta.db_table
            if collection_name in db.list_collection_names():
                db.drop_collection(collection_name)


        # Re-create Teams with explicit IDs
        marvel = Team.objects.create(id=1, name='Team Marvel')
        dc = Team.objects.create(id=2, name='Team DC')

        # Users with explicit IDs
        users = [
            User(id=1, email='ironman@marvel.com', username='ironman', team=marvel),
            User(id=2, email='captain@marvel.com', username='captain', team=marvel),
            User(id=3, email='batman@dc.com', username='batman', team=dc),
            User(id=4, email='superman@dc.com', username='superman', team=dc),
        ]
        for user in users:
            user.set_password('password123')
            user.save()

        # Activities with explicit IDs
        Activity.objects.create(id=1, user=users[0], type='run', duration=30, distance=5)
        Activity.objects.create(id=2, user=users[1], type='cycle', duration=45, distance=15)
        Activity.objects.create(id=3, user=users[2], type='swim', duration=25, distance=1)
        Activity.objects.create(id=4, user=users[3], type='run', duration=60, distance=10)

        # Workouts with explicit IDs
        Workout.objects.create(id=1, name='Morning Cardio', description='30 min run + 15 min cycle')
        Workout.objects.create(id=2, name='Strength', description='Pushups, Pullups, Squats')

        # Leaderboard with explicit IDs
        Leaderboard.objects.create(id=1, user=users[0], points=100)
        Leaderboard.objects.create(id=2, user=users[1], points=90)
        Leaderboard.objects.create(id=3, user=users[2], points=80)
        Leaderboard.objects.create(id=4, user=users[3], points=70)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))

        # Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Users
        users = [
            User(email='ironman@marvel.com', username='ironman', team=marvel),
            User(email='captain@marvel.com', username='captain', team=marvel),
            User(email='batman@dc.com', username='batman', team=dc),
            User(email='superman@dc.com', username='superman', team=dc),
        ]
        for user in users:
            user.set_password('password123')
            user.save()

        # Activities
        Activity.objects.create(user=users[0], type='run', duration=30, distance=5)
        Activity.objects.create(user=users[1], type='cycle', duration=45, distance=15)
        Activity.objects.create(user=users[2], type='swim', duration=25, distance=1)
        Activity.objects.create(user=users[3], type='run', duration=60, distance=10)

        # Workouts
        Workout.objects.create(name='Morning Cardio', description='30 min run + 15 min cycle')
        Workout.objects.create(name='Strength', description='Pushups, Pullups, Squats')

        # Leaderboard
        Leaderboard.objects.create(user=users[0], points=100)
        Leaderboard.objects.create(user=users[1], points=90)
        Leaderboard.objects.create(user=users[2], points=80)
        Leaderboard.objects.create(user=users[3], points=70)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))

# Models for reference (should exist in octofit_tracker/models.py):
# class Team(models.Model):
#     name = models.CharField(max_length=100)
#
# class Activity(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     type = models.CharField(max_length=50)
#     duration = models.IntegerField()
#     distance = models.FloatField()
#
# class Workout(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#
# class Leaderboard(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     points = models.IntegerField()
