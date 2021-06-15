from django.urls import path
from . import views
urlpatterns = [
    path('', views.NumberChildren.as_view()),
]
