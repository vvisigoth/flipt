from django.shortcuts import render_to_response
from theater.models import Module
from theater.config import playlist

# Create your views here.

def index(request):
  #playlist = playlist
  return render_to_response('theater/index.html', {'playlist': playlist})
