from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , Http404

# Create your views here.

articles = {
    'sports' : 'This is the sports news',
    'politics' : 'This is the politics news',
    'business' : 'This is the business news',
    'technology' : 'This is the technology news',
}



def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        raise Http404("404 ")



def add_view(request, num1, num2):
    #
    add_result = num1 + num2
    result = f'The sum of {num1} and {num2} is {add_result}'
    return HttpResponse(result)