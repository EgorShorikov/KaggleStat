from django.shortcuts import render
from .models import Contest, LeaderBoard
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SearchTeamForm, SearchCompetitionForm
import json


def index(request):
    return render(request, 'homepage/index.html')


def dashboard_list(request):
    template = 'dashboard/index.html'
    contests = Contest.objects.all()
    paginator = Paginator(contests, 21)
    page = request.GET.get('page')

    try:
        context = paginator.page(page)
    except PageNotAnInteger:
        context = paginator.page(1)
    except EmptyPage:
        context = paginator.page(paginator.num_pages)

    context = {'competitions': context}
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
                            snapshot.saved_at.strftime('%Y-%m-%d %H:%M')
                        )
                        positions.append(int(lb['position']))
                        scores.append(float(lb['score']))
                        break
                else:
                    labels.append(snapshot.saved_at.strftime('%Y-%m-%d %H:%M'))
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
