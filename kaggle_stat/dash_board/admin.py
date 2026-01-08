from django.contrib import admin
from .models import Contest, Team, LeaderBoard
 

admin.site.register(Contest)
admin.site.register(Team)
# admin.site.register(KaggleUser)
# admin.site.register(ParticipantContest)
admin.site.register(LeaderBoard)
