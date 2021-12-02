from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

challenges_text = {
    'january': 'Follow the Django course at least 30 min a day',
    'february': 'Work on internship for 1 hour a day',
    'march': 'Read 1 hour a day',
    'april': 'Follow the Django course at least 30 min a day',
    'may': 'Work on internship for 1 hour a day',
    'june': 'Read 1 hour a day',
    'july': 'Follow the Django course at least 30 min a day',
    'august': 'Work on internship for 1 hour a day',
    'september': 'Read 1 hour a day',
    'october': 'Follow the Django course at least 30 min a day',
    'november': 'Work on internship for 1 hour a day',
    'december': None,
}

def index(request):
    list_items = ""
    months = list(challenges_text.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_integer(request, month):
    months = list(challenges_text.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = challenges_text[month]
        return render(request, 'challenges/challenge.html', {
            'month_name': month,
            'text': challenge_text
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
    