from django.shortcuts import render_to_response
from theater.models import Module
from theater.config import playlist
import re

# Create your views here.

def index(request):
  #make some logic here (or config) that will be smart about getting the raw ur
  #plist = []
  #for i in playlist:
    #ifrm_guts = re.findall(r'(src ?= ?")(\S+)(")', i)
    #plist.append(ifrm_guts[1])
  return render_to_response('theater/index.html', {'playlist': playlist})
