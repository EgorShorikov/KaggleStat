from django.core.management.base import BaseCommand
import time
from django.db.models import Max
from kaggle_service import KaggleService
from dash_board.models import Contest, LeaderBoard


class Command(BaseCommand):
    help = 'Загрузка лидербордов'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=200,
            help='Количество участников'
        )

    def handle(self, *args, **options):
        service = KaggleService()
        competitions = Contest.objects.all()
        current_version = LeaderBoard.objects.aggregate(
            max_version=Max('version')
        )['max_version']

        for competition in competitions:
            submissions = service.get_top_n_leaderboard(
                competition.competition_slug,
                options['count']
            )

            leaderboard_data = []
            for position, submission in enumerate(submissions, start=1):
                leaderboard_data.append({
                    'team_id': submission.team_id,
                    'team_name': submission.team_name,
                    'score': submission.score,
                    'position': position,
                })

            LeaderBoard.objects.create(
                contest_id=competition,
                data={"leaderboard": leaderboard_data},
                version=current_version + 1
            )

            time.sleep(1.75)
            self.stdout.write(f'Загружен лидерборд для {
                competition.competition_slug
            }')

        self.stdout.write(f'Загружено лидербордов: {competitions.count()}')
