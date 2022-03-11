from django.shortcuts import get_object_or_404, render
from .models import Youtuber
# Create your views here.

def youtubers(request):
 tubers=Youtuber.objects.order_by('-created_date')
 city_search= Youtuber.objects.values_list('city',flat=True).distinct()
 camera_type_search= Youtuber.objects.values_list('camera_type',flat=True).distinct()
 catogary_search= Youtuber.objects.values_list('catogary',flat=True).distinct()
 
 
 if 'keyword' in request.GET:
  keyword=request.GET['keyword']
  if keyword:
   tubers=tubers.filter(description__icontains=keyword)

 if 'city' in request.GET:
  city=request.GET['city']
  if city:
   tubers=tubers.filter(city__iexact=city)

 
 if 'camera_type' in request.GET:
  camera_type=request.GET['camera_type']
  if camera_type:
   tubers=tubers.filter(camera_type__iexact=camera_type)

 
 if 'catogary' in request.GET:
  catogary=request.GET['catogary']
  if catogary:
   tubers=tubers.filter(catogary__iexact=catogary)

 data={
  'tuber':tubers,
  'city_search':city_search,
  'camera_type_search':camera_type_search,
  'catogary_search':catogary_search,

 }
 return render(request,'youtubers/youtubers.html',data)

def youtubers_details(request,id):
 details=get_object_or_404(Youtuber, pk=id)
 data={
  'tuber':details,
 }
 return render(request,'youtubers/youtubers_details.html',data)

def search(request):
 tubers=Youtuber.objects.order_by('-created_date')
  # values of model class
 city_search= Youtuber.objects.values_list('city',flat=True).distinct()
 camera_type_search= Youtuber.objects.values_list('camera_type',flat=True).distinct()
 catogary_search= Youtuber.objects.values_list('catogary',flat=True).distinct()
 
 
 if 'keyword' in request.GET:
  keyword=request.GET['keyword']
  if keyword:
   tubers=tubers.filter(description__icontains=keyword)

 if 'city' in request.GET:
  city=request.GET['city']
  if city:
   tubers=tubers.filter(city__iexact=city)

 
 if 'camera_type' in request.GET:
  camera_type=request.GET['camera_type']
  if camera_type:
   tubers=tubers.filter(camera_type__iexact=camera_type)

 
 if 'catogary' in request.GET:
  catogary=request.GET['catogary']
  if catogary:
   tubers=tubers.filter(catogary__iexact=catogary)

 data={
  'tuber':tubers,
  'city_search':city_search,
  'camera_type_search':camera_type_search,
  'catogary_search':catogary_search,

 }
 return render(request,'youtubers/search.html',data)