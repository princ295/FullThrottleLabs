
from .models import ActivityPeriod, Period
from rest_framework import serializers


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ['start_time', 'end_time']


class ActivityPeriodSerializer(serializers.ModelSerializer):
    activity_periods = PeriodSerializer(many=True, read_only=True)
    class Meta:
        model = ActivityPeriod
        fields = ['real_name', 'tz','activity_periods']



