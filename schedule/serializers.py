from rest_framework import serializers

from .models import Week, Child

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Week
        fields = (
            'child',
            'start_date',
            'end_date', 
            'registered',
        )