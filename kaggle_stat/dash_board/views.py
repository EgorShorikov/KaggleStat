from django.shortcuts import render
from .models import Contest, LeaderBoard
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    # valid_competition_groups = ["general", "entered", "community", "hosted", "unlaunched", "unlaunched_community"]
    # valid_competition_categories = [
    #     "unspecified",
    #     "featured",
    #     "research",
    #     "recruitment",
    #     "gettingStarted",
    #     "masters",
    #     "playground",
    # ]
    # valid_competition_sort_by = [
    #     "grouped",
    #     "best",
    #     "prize",
    #     "earliestDeadline",
    #     "latestDeadline",
    #     "numberOfTeams",
    #     "relevance",
    #     "recentlyCreated",
    # ]
    # group = request.GET.get('group', '')
    # category = request.GET.get('category', '')
    # sort_by = request.GET.get('sort_by', '')


    template = 'homepage/index.html'
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


def dashboard(request, dashboard_slug):
    contest = Contest.objects.get(competition_slug=dashboard_slug)
    data = (LeaderBoard.objects
                       .filter(contest_id=contest.id))
    template = 'homepage/dashboard.html'
    context = {'dashboard': data}
    return render(request, template, context)
