from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('api/v1/',views.NumberChildren.as_view()),
    path('schedule/', views.schedule, name='schedule')
]
