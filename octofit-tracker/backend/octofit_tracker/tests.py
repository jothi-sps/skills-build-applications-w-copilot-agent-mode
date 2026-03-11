from rest_framework.test import APITestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserTests(APITestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser', email='test@example.com')
        self.assertEqual(user.username, 'testuser')

class TeamTests(APITestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityTests(APITestCase):
    def test_create_activity(self):
        user = User.objects.create(username='activityuser', email='activity@example.com')
        activity = Activity.objects.create(user=user, activity_type='Run', duration=30, calories=200, date='2023-01-01')
        self.assertEqual(activity.activity_type, 'Run')

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Morning Routine', description='A simple workout', suggested_for='Beginner')
        self.assertEqual(workout.name, 'Morning Routine')

class LeaderboardTests(APITestCase):
    def test_create_leaderboard(self):
        user = User.objects.create(username='leaderuser', email='leader@example.com')
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)
