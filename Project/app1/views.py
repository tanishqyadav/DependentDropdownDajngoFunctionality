from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.


def get_states(request):
    country_id = request.GET['country_id']
    get_country = Country.objects.get(id=country_id)
    state = State.objects.filter(country=get_country)
    return render(request, 'get-states.html', locals())

def get_cities(request):
    state_id = request.GET['state_id']
    get_state = State.objects.get(id=state_id)
    city = District.objects.filter(state=get_state)
    return render(request, 'get-cities.html', locals())

def get_business(request):
    city_id = request.GET['city_id']
    get_city = District.objects.get(id=city_id)
    business = Business.objects.filter(city=get_city)
    return render(request, 'get-business.html', locals())

def get_package(request):
    business_id = request.GET['business_id']
    get_business = Business.objects.get(id=business_id)
    package = Package.objects.filter(business=get_business)
    return render(request, 'get-package.html', locals())

def dependantfield(request):
    country = Country.objects.all()
    return render(request, 'dependantfield.html', locals())


def possitiveorder(request):
     ans = []
     lst = [5,6]
     for i in range(10):
          ans.append(i)
     
     for i in range(len(lst)):
          ans.remove(lst[i])
    
     print(ans)
     return HttpResponse(ans)
