from django.shortcuts import render
from django.template import loader
from django.db.models import Count
from django.http import HttpResponse

from .serializers import ScheduleSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Week, Child

# from json import dumps

# Create your views here
def home(response):
    return render(response, "schedule/home.html")

def schedule(response):
    return render(response, "schedule/calendar.html")

def aboutus(response):
    return render(response, "schedule/aboutus.html")

def signup(response):
    return render(response, 'schedule/signup.html')

class NumberChildren(APIView):
    def get(self, request, format=None):
        week = Week.objects.annotate(num_child = Count('child'))
        serializer = ScheduleSerializer(week, many=True)
        return Response(serializer.data)




# def schedule(request):
#     schedule = Week.objects.annotate(num_child = Count('child'))
# makes the same query as a .all query, but adds new field that can be accessed (based off existing field)
    # context = {
    #     'schedule': schedule
    # }
 # dump data
    # dataJSON = dumps(context)
    # return render(request, 'schedule/calendar.html', {'data': dataJSON})