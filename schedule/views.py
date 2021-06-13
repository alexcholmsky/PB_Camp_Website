from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse
from .models import Week, Child

# Create your views here.
def schedule(request):
    schedule = Week.objects.all()
    context = {
        'schedule': schedule,
    
    }
    return render(request, 'schedule/calendar.html',context)