from django.core.management.base import BaseCommand
from kaggle_service import KaggleService
from dash_board.models import Contest


class Command(BaseCommand):
    help = 'Загрузка конкурсов'

    def handle(self, *args, **options):
        service = KaggleService()
        competitions = service.get_n_pages_competitions(
            1, 36, sort_by='relevance'
        )

        for competition in competitions:
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

        self.stdout.write(f'Загружено {len(competitions)} соревнований')
