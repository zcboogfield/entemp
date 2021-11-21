from Django.shortcuts import render
from Django.http import HttpResponse


def entemp_view(request):
    source_url = 'https://psl.noaa.gov/boulder/data.daily.html'
    return HttpResponse ("Hello World" + source_url)
