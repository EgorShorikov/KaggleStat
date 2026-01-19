from django.core.management.base import BaseCommand
from kaggle_service import KaggleService
from dash_board.models import Contest


class Command(BaseCommand):
    help = 'Загрузка конкурсов'

    def add_arguments(self, parser):
        parser.add_argument(
            '--from-page',
            type=int,
            default=1,
            help='С страницы'
        )
        parser.add_argument(
            '--to-page',
            type=int,
            default=36,
            help='По страницу'
        )

    def handle(self, *args, **options):
        service = KaggleService()
        competitions = service.get_n_pages_competitions(
            options['from_page'], options['to_page'], sort_by='relevance'
        )
        for competition in competitions:
            print(competition.thumbnail_image_url)
            Contest.objects.update_or_create(
                competition_slug=competition.ref.split('/')[-1],
                defaults={
                    'title': competition.title,
                    'participant_count': competition.team_count,
                    'deadline': competition.deadline,
                    'prize': competition.reward,
                    'description': competition.description,
                    'image_url': competition.thumbnail_image_url,
                    'url': competition.url,
                    'organization_name': competition.organization_name,
                    'organization_ref': competition.organization_ref
                }
            )

        self.stdout.write(f'Загружено {len(competitions)} соревнований')
