import os
import sys
import django
import time
from django.db.models import Max


sys.path.append(r'C:\Users\user\Desktop\KaggleStat\kaggle_stat')
os.environ['DJANGO_SETTINGS_MODULE'] = 'kaggle_stat.settings'
django.setup()

from kaggle_service import KaggleService
from dash_board.models import Contest, LeaderBoard


class Worker:
    def __init__(self):
        self.service = KaggleService()


    def load_n_pages_competitions(self, n_pages):
        competitions = self.service.get_n_pages_competitions(n_pages=n_pages, sort_by='relevance')
        for competition in competitions:
            Contest.objects.update_or_create(
                kaggle_slug=competition.ref.split('/')[-1],
                defaults={
                    'title': competition.title,
                    'deadline': competition.deadline,
                    'participant_count': competition.team_count,
                    'prize': competition.reward,
                    'description': competition.description,
                    'image_url': competition.thumbnail_image_url
                }
            )

    def load_leaderboard(self):
        competitions = Contest.objects.all()
        current_version = LeaderBoard.objects.aggregate(max_version=Max('version'))['max_version']
        for competition in competitions:
            competition_slug = competition.competition_slug
            submissions = self.service.get_top_n_leaderboard(competition_slug, 50)

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


if __name__ == "__main__":
    worker = Worker()
    # worker.load_leaderboard()
    # worker.load_n_pages_competitions(35)
