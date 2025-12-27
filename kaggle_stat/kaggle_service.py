import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi, ApiGetLeaderboardRequest, ApiCompetition
from kagglesdk.competitions.services.competition_api_service import CompetitionApiClient
import time
api = KaggleApi()
api.authenticate()


# comp_ref = competitions.competitions[0].ref
# id (int)
#     ref (str)
#     title (str)
#     url (str)
cnt = 0
cnt1 = 0
token = None
comp = ApiCompetition()
a = api.competition_leaderboard_view
comp.submissions_disabled = False
# competitions = api.competitions_list(page=4)
for page in range(1, 20):
    print(page)
    competitions = api.competitions_list(page=page)
    for x in range(len(competitions.competitions)):
        if competitions.competitions[x].submissions_disabled == True:
            print(competitions.competitions[x].url.split('/')[-1])
    time.sleep(1)
    # print(competitions.competitions[x].submissions_disabled)
# with api.build_kaggle_client() as kaggle:
#     request = ApiGetLeaderboardRequest()
#     request.competition_name = 'gemini-3'
#     request.page_size = 30
#     # request.page_token = page_token
#     response = kaggle.competitions.competition_api_client.get_leaderboard(request)
#     print(response.submissions[0:10])
# for page in range(10):
#     competitions = api.competitions_list(page_token=token)
#     for x in range(20):
#         try:
#             comp_title = competitions.competitions[x].url.split('/')[-1]
#             # print(comp_title)
#             with api.build_kaggle_client() as kaggle:
#                 request = ApiGetLeaderboardRequest()
#                 request.competition_name = 'data-science-bowl-2019'
#                 request.page_size = 30
#                 # request.page_token = page_token
#                 response = kaggle.competitions.competition_api_client.get_leaderboard(request)
#                 print(response.submissions[0])
#                 cnt += 1
#                 print(cnt, cnt1)
#         except Exception:
#             cnt1+=1
#     token = competitions.next_page_token
# print(cnt)
# print(comp_ref)
# print(competitions.)
# token = None

# for x in range(1,10):
#     leaderboard = api.competition_leaderboard_view(
#     competition="titanic"
#     page_token=token
#     )
#     print(leaderboard)
#     token = 

# b = CompetitionApiClient().get_leaderboard(ApiGetLeaderboardRequest(competition_name='titanic'))


# with api.build_kaggle_client() as kaggle:
#     request = ApiGetLeaderboardRequest()
#     request.competition_name = 'vesuvius-challenge-surface-detection'
#     request.page_size = 30
#     # request.page_token = page_token
#     response = kaggle.competitions.competition_api_client.get_leaderboard(request)
#     print(response)

# b = api.competition_submissions(competition='bus-delay-starter')

# print(b)

