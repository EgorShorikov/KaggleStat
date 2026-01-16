import os
import sys
import django
import time
from django.db.models import Max


sys.path.append(r'C:\Users\user\Desktop\KaggleStat\kaggle_stat')
os.environ['DJANGO_SETTINGS_MODULE'] = 'kaggle_stat.settings'
django.setup()

from kaggle_service import KaggleService
from dash_board.models import Contest, LeaderBoard, Team


class Worker:
    def __init__(self):
        self.service = KaggleService()


    def load_n_pages_competitions(self, start_page, end_page):
        competitions = self.service.get_n_pages_competitions(start_page, end_page, sort_by='relevance')
        for competition in competitions:
            print(competition)
            Contest.objects.update_or_create(
                competition_slug=competition.ref.split('/')[-1],
                defaults={
                    'title': competition.title,
                    'deadline': competition.deadline,
                    'participant_count': competition.team_count,
                    'prize': competition.reward,
                    'description': competition.description,
                    'image_url': competition.thumbnail_image_url,
                    'url': competition.url,
                    'organization_name': competition.organization_name,
                    'organization_ref': competition.organization_ref
                }
            )

    def load_leaderboard(self, participant_count):
        competitions = Contest.objects.all()
        current_version = LeaderBoard.objects.aggregate(max_version=Max('version'))['max_version']
        for competition in competitions:
            competition_slug = competition.competition_slug
            submissions = self.service.get_top_n_leaderboard(competition_slug, participant_count)

            leaderboard_data = []
            for position, submission in enumerate(submissions, start=1):
                leaderboard_data.append({
                    'team_id': submission.team_id,
                    'team_name': submission.team_name,
                    'score': submission.score,
                    'position': position,
                })
            leaderboard = {"leaderboard": leaderboard_data}

            contest = Contest.objects.get(competition_slug=competition_slug)

            LeaderBoard.objects.create(
                contest_id=contest,
                data=leaderboard,
                version=current_version + 1
            )
            time.sleep(1.25)

    def load_teams(self):
        current_version = (LeaderBoard.objects
                                      .aggregate(max_version=Max('version'))
                                      ['max_version'])
        leaderboards = (LeaderBoard.objects
                                   .values('contest_id', 'data')
                                   .filter(version=current_version))
        team_id_contests = {}
        for lb in leaderboards:
            contest_id = lb['contest_id']
            entries = lb['data']['leaderboard']
            if len(entries) > 0:
                for entry in entries:
                    team_id = entry['team_id']
                    team_name = entry['team_name']

                    if team_id not in team_id_contests:
                        team_id_contests[team_id] = []
                    team_id_contests[team_id].append(contest_id)

                    Team.objects.update_or_create(
                        team_id=team_id,
                        defaults={
                            'team_slug': team_name,
                        }
                    )

        for team_id, contests in team_id_contests.items():
            team = Team.objects.get(team_id=team_id)
            contest = Contest.objects.filter(id__in=contests)
            team.contests.add(*contest)


if __name__ == "__main__":
    worker = Worker()
    worker.load_leaderboard(100)
    # worker.load_n_pages_competitions(1, 5)
    # worker.load_teams()
    # teams = Team.objects.filter(team_slug='tascj')

    # print(f"Найдено команд: {teams.count()}")

    # for team in teams:
    #     print(f"\nКоманда ID: {team.team_id}")
    #     contests = team.contests.all()
    #     print(f"Контестов у этой команды: {contests.count()}")

    #     for contest in contests[:3]:  # Первые 3 контеста
    #         print(f"  - {contest.competition_slug}")
