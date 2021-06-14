from django.shortcuts import render
from django.template import loader
from django.db.models import Count
from django.http import HttpResponse

from .serializers import ScheduleSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Week, Child

# Create your views here
def schedule(request):
    schedule = Week.objects.annotate(num_child = Count('child'))
# makes the same query as a .all query, but adds new field that can be accessed (based off existing field)
    context = {
        'schedule': schedule
    }
    return render(request, 'schedule/calendar.html', context)

# class NumberChildren(APIView):
#     def get(self, request, format=None):
#         week = Week.objects.annotate(num_child = Count('child'))
#         serializer = ScheduleSerializer(week, many=True)
#         return Response(serializer.data)