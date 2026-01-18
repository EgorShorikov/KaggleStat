from django.contrib import admin
from .models import Contest, Team, LeaderBoard


@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = ['competition_slug', 'title', 'deadline', 'prize']

    search_fields = ['competition_slug', 'title', 'organization_name']

    list_filter = ['deadline']

    ordering = ['-deadline']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_id', 'team_slug']

    search_fields = ['team_slug', 'team_id']

    filter_horizontal = ['contests']


@admin.register(LeaderBoard)
class LeaderBoardAdmin(admin.ModelAdmin):
    list_display = ['contest_id', 'saved_at', 'version']

    search_fields = ['contest_id__title', 'contest_id__competition_slug']

    list_filter = ['saved_at', 'contest_id']

    ordering = ['-saved_at']

    date_hierarchy = 'saved_at'
