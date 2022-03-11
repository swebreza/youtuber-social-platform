from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Slider,Team
from youtubers.models import Youtuber
# Create your views here.
def home(request):
  Sliders=Slider.objects.all()
  teams = Team.objects.all()
  featured_youtuber=Youtuber.objects.order_by('-created_date').filter(is_featured = True)
  youtubers=Youtuber.objects.all()
  data={
    'sliders':Sliders,
    'teamss':teams,
    'featured_youtuber':featured_youtuber,
    'youtubers':youtubers,
  }
  return render(request,'webpages/home.html',data)

def about(request):
  teams = Team.objects.all()
  data={
    'teamss':teams,
  }
  return render(request,'webpages/about.html',data)


def services(request):
 return render(request,'webpages/services.html')

def contact(request):
  return render(request,'webpages/contact.html')

# def out(request):
#     return HttpResponseRedirect("http://google.com")