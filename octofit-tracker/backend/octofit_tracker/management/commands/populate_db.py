from django.core.management.base import BaseCommand
from datetime import date
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()
        Workout.objects.all().delete()

        # Create superhero users
        self.stdout.write('Creating users...')
        users_data = [
            {'username': 'superman', 'email': 'superman@dc.com', 'password': 'krypton123'},
            {'username': 'batman', 'email': 'batman@dc.com', 'password': 'gotham123'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com', 'password': 'themyscira123'},
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'password': 'stark123'},
            {'username': 'captainamerica', 'email': 'captainamerica@marvel.com', 'password': 'shield123'},
            {'username': 'blackwidow', 'email': 'blackwidow@marvel.com', 'password': 'natasha123'},
        ]

        users = {}
        for data in users_data:
            user = User.objects.create(**data)
            users[data['username']] = user
            self.stdout.write(f'  Created user: {user.username}')

        # Create teams
        self.stdout.write('Creating teams...')
        team_dc = Team.objects.create(name='Team DC')
        team_dc.members.add(users['superman'], users['batman'], users['wonderwoman'])

        team_marvel = Team.objects.create(name='Team Marvel')
        team_marvel.members.add(users['ironman'], users['captainamerica'], users['blackwidow'])

        self.stdout.write(f'  Created team: {team_dc.name}')
        self.stdout.write(f'  Created team: {team_marvel.name}')

        # Create activities
        self.stdout.write('Creating activities...')
        activities_data = [
            {'user': users['superman'], 'activity_type': 'Flying', 'duration': 60, 'date': date(2025, 4, 1)},
            {'user': users['batman'], 'activity_type': 'Martial Arts', 'duration': 90, 'date': date(2025, 4, 1)},
            {'user': users['wonderwoman'], 'activity_type': 'Sword Training', 'duration': 75, 'date': date(2025, 4, 2)},
            {'user': users['ironman'], 'activity_type': 'Suit Testing', 'duration': 45, 'date': date(2025, 4, 2)},
            {'user': users['captainamerica'], 'activity_type': 'Shield Throwing', 'duration': 60, 'date': date(2025, 4, 3)},
            {'user': users['blackwidow'], 'activity_type': 'Stealth Training', 'duration': 80, 'date': date(2025, 4, 3)},
        ]

        for data in activities_data:
            activity = Activity.objects.create(**data)
            self.stdout.write(f'  Created activity: {activity}')

        # Create leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        leaderboard_data = [
            {'user': users['superman'], 'score': 100},
            {'user': users['batman'], 'score': 95},
            {'user': users['wonderwoman'], 'score': 90},
            {'user': users['ironman'], 'score': 85},
            {'user': users['captainamerica'], 'score': 80},
            {'user': users['blackwidow'], 'score': 75},
        ]

        for data in leaderboard_data:
            entry = Leaderboard.objects.create(**data)
            self.stdout.write(f'  Created leaderboard entry: {entry}')

        # Create workouts
        self.stdout.write('Creating workouts...')
        workouts_data = [
            {'name': 'Super Strength', 'description': 'A workout routine to build super strength like Superman.', 'duration': 60},
            {'name': 'Bat Agility', 'description': 'Agility and stealth training inspired by Batman.', 'duration': 45},
            {'name': 'Amazon Warrior', 'description': 'Combat and endurance training inspired by Wonder Woman.', 'duration': 75},
            {'name': 'Iron Endurance', 'description': 'High-tech endurance training inspired by Iron Man.', 'duration': 50},
            {'name': 'Shield Defense', 'description': 'Defensive training inspired by Captain America.', 'duration': 55},
        ]

        for data in workouts_data:
            workout = Workout.objects.create(**data)
            self.stdout.write(f'  Created workout: {workout.name}')

        self.stdout.write(self.style.SUCCESS('Successfully populated the octofit_db database!'))
