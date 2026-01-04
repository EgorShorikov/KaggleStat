import os
import sys
import django


sys.path.append(r'C:\Users\user\Desktop\KaggleStat\kaggle_stat')
os.environ['DJANGO_SETTINGS_MODULE'] = 'kaggle_stat.settings'
django.setup()

from kaggle_service import KaggleService
from dash_board.models import Contest


def run():
    service = KaggleService()
    # Base.metadata.create_all(engine)
    competitions = service.get_all_competitions()
    
    for competition in competitions:
        print(competition.reward)
        Contest.objects.update_or_create(
            kaggle_slug=competition.ref.split('/')[-1],
            defaults={
                'title': competition.title,
                'deadline': competition.deadline,
                'participant_count': competition.team_count,
                'prize': competition.reward,
                'description': competition.description
            }
        )
    #     cursor.execute('''
    #         INSERT OR REPLACE INTO Contest (kaggle_slug,
    #                                              title,
    #                                              deadline,
    #                                              participant_count,
    #                                              prize,
    #                                              description)
    #         VALUES (?, ?, ?, ?, ?, ?)
    #     ''', (competition.ref.split('/')[-1],
    #           competition.title,
    #           competition.deadline,
    #           competition.team_count,
    #           competition.reward,
    #           competition.description
    #           ))
    # lb = service.get_top_20_leaderboard('titanic')
    # if lb:
    #     cursor.execute('DELETE FROM leaderboard WHERE comp_id = "titanic"')
    #     for entry in lb:
    #         cursor.execute('''
    #             INSERT INTO leaderboard (comp_id, team, score)
    #             VALUES (?, ?, ?)
    #         ''', ('titanic', entry.teamName, entry.score))

    print("OK")


if __name__ == "__main__":
    run()
