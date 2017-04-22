from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import QueryDict
import requests

# Create your views here.
def index(request):
    return render(request, 'site_app/index.html', {})

def discover(request):
    query = request.META['QUERY_STRING']
    querydict = QueryDict(query)
    congressUrl = 'https://congress.api.sunlightfoundation.com/legislators/locate?zip=' + querydict.get('zip') + '&apikey=d53d3b6bf3564300aeb620b05566667d'
    response = requests.get(congressUrl)
    # localUrl = 'https://openstates.org/api/v1/METHOD/'

    t = TemplateResponse(request, 'site_app/discover.html', response.json())
    return t.render()