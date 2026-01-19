from kaggle.api.kaggle_api_extended import KaggleApi, ApiGetLeaderboardRequest
import time
from kagglesdk.competitions.types.competition_api_service import ApiGetCompetitionRequest


class KaggleService:

    def __init__(self, api=None):
        self.api = api or KaggleApi()
        self.api.authenticate()

    def get_n_pages_competitions(
        self,
        start_page,
        end_page,
        search=None,
        group=None,
        category=None,
        sort_by=None
    ):
        competitions_updated = []
        for page in range(start_page, end_page + 1):
            try:
                response = self.api.competitions_list(
                    page=page,
                    search=search,
                    group=group,
                    category=category,
                    sort_by=sort_by
                )

                if response is None:
                    break

                for competition in response.competitions:
                    if not competition.submissions_disabled:
                        time.sleep(1.5)
                        competitions_updated.append(
                            self.get_competition_by_name(competition.ref.split('/')[-1])
                        )
                time.sleep(2)

            except Exception as e:
                return competitions_updated

        return competitions_updated

    def get_competition_by_name(self, competition_slug):
        with self.api.build_kaggle_client() as kaggle_client:
            request = ApiGetCompetitionRequest()
            request.competition_name = competition_slug
            comp_info = (
                kaggle_client
                .competitions
                .competition_api_client
                .get_competition(request)
            )
            return comp_info

    def search_by_name_in_leaderboard(self, competition_slug, team_name):
        page_token = None
        while True:
            with self.api.build_kaggle_client() as kaggle_client:
                request = ApiGetLeaderboardRequest()
                request.competition_name = competition_slug
                request.page_size = 20
                request.page_token = page_token
                leaderboard = (
                    kaggle_client
                    .competitions
                    .competition_api_client
                    .get_leaderboard(request)
                )

            for team_data in leaderboard.submissions:

                if team_name == team_data.team_name:
                    return (team_data.submission_date, team_data.score)

            if leaderboard.next_page_token == "":
                return 'Not Found'

            page_token = leaderboard.next_page_token
            time.sleep(0.1)

    def get_top_n_leaderboard(self, competition_slug, n):
        competition = self.api.competition_leaderboard_view(competition_slug, page_size=n)
        return competition
