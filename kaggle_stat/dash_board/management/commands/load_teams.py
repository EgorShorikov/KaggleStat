from django.core.management.base import BaseCommand
from django.db.models import Max
from dash_board.models import LeaderBoard, Team, Contest


class Command(BaseCommand):
    help = 'Загрузка команд'

    def handle(self, *args, **options):
        current_version = LeaderBoard.objects.aggregate(
            max_version=Max('version')
        )['max_version']
        leaderboards = (LeaderBoard.objects
                                   .values('contest_id', 'data')
                                   .filter(version=current_version))

        team_id_contests = {}
        for lb in leaderboards:
            contest_id = lb['contest_id']
            entries = lb['data']['leaderboard']

            for entry in entries:
                team_id = entry['team_id']
                team_name = entry['team_name']

                if team_id not in team_id_contests:
                    team_id_contests[team_id] = []
                team_id_contests[team_id].append(contest_id)

                Team.objects.update_or_create(
                    team_id=team_id,
                    defaults={'team_slug': team_name}
                )

        for team_id, contests in team_id_contests.items():
            team = Team.objects.get(team_id=team_id)
            contest_objects = Contest.objects.filter(id__in=contests)
            team.contests.add(*contest_objects)

        self.stdout.write(f'Обработано {len(team_id_contests)} команд')
