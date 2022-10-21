from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges_dict = {
    'january': 'Jan!',
    'february': 'Feb!',
    'march': 'Mar!',
    'april': 'Apr!',
    'may': 'May!',
    'june': 'Jun!',
    'july': 'Jul!',
    'august': 'Aug!',
    'september': 'Sept!',
    'october': 'Oct!',
    'november': 'Nov!',
    'december': None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges_dict.keys())
    return render(request, 'challenges/index.html', {
        'months': months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges_dict.keys())
    try:
        redirect_month = months[month-1]
        redirect_path = reverse('month-challenge', args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
        #return HttpResponseRedirect('/challenges/' + redirect_month)
    except:
        raise Http404()
        #return HttpResponseNotFound('<h1>This month is not supported!<h1>')

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        return render(request, 'challenges/challenge.html', {
            'text':challenge_text,
            'month': month
        })
        #response_data = render_to_string('challenges/challenge.html')
        #response_data = f'<h1>{challenge_text}</h1>'
        #return HttpResponse(response_data)
    except:
        raise Http404() # change DEBUG = TRUE after development, it would show the 404 templates
        #response_data = render_to_string('404.html')
        #return HttpResponse(response_data)
        #return HttpResponseNotFound('<h1>This month is not supported!<h1>')


"""
def january(request):
    return HttpResponse("Jan!")

def index(request):
    list_items = ''
    months = list(monthly_challenges_dict.keys())

    for month in months:
        month_path = reverse('month-challenge', args=[month])
        capitalized_month = month.capitalize()
        list_items += f'<li><a href=\'{month_path}\'>{capitalized_month}</a></li>'
    
    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)
"""