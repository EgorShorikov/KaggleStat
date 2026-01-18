from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Contest, LeaderBoard
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SearchTeamForm, ContestSearchForm
import json


def index(request):
    form = ContestSearchForm()

    if request.method == 'GET' and 'team_slug' in request.GET:
        form = ContestSearchForm(request.GET)
        if form.is_valid():
            team_slug = form.cleaned_data['team_slug']
            return redirect(f'/dashboard/?team_slug={team_slug}')

    context = {'form': form}
    return render(request, 'homepage/index.html', context)


def dashboard_list(request):
    team_slug = request.GET.get('team_slug', '')

    contests = Contest.objects.all()
    if team_slug:
        contests = contests.filter(
            Q(team__team_slug__icontains=team_slug)
        ).distinct()

    paginator = Paginator(contests, 21)
    page = request.GET.get('page')

    try:
        competitions = paginator.page(page)
    except PageNotAnInteger:
        competitions = paginator.page(1)
    except EmptyPage:
        competitions = paginator.page(paginator.num_pages)

    context = {
        'competitions': competitions,
        'search_query': team_slug,
    }
    template = 'dashboard/index.html'

    return render(request, template, context)


def dashboard_detail(request, dashboard_slug):
    contest = Contest.objects.get(competition_slug=dashboard_slug)
    form = SearchTeamForm(request.GET or None)
    labels = []
    positions = []
    scores = []
    searched_team = None

    if request.GET and form.is_valid():
        searched_team = form.cleaned_data.get('team_name')
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')

        if searched_team:
            query_set = LeaderBoard.objects.filter(
                contest_id=contest.id,
                saved_at__range=[start_date, end_date]
            )
            for snapshot in query_set:
                for lb in snapshot.data['leaderboard']:
                    if lb['team_name'].lower() == searched_team.lower():
                        labels.append(
                            snapshot.saved_at.strftime('%d.%m.%Y %H:%M')
                        )
                        positions.append(int(lb['position']))
                        scores.append(float(lb['score']))
                        break
                else:
                    labels.append(snapshot.saved_at.strftime('%d.%m.%Y %H:%M'))
                    positions.append(None)
                    scores.append(None)

    context = {
        'labels': json.dumps(labels),
        'positions': json.dumps(positions),
        'scores': json.dumps(scores),
        'searched_team': searched_team,
        'form': form,
        'contest': contest,
    }
    template = 'dashboard/dashboard.html'
    return render(request, template, context)
