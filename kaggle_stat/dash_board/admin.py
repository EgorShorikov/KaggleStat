from django.contrib import admin
from .models import Contest, KaggleUser, ParticipantContest, LeaderBoard
 

admin.site.register(Contest)
admin.site.register(KaggleUser)
admin.site.register(ParticipantContest)
admin.site.register(LeaderBoard)
