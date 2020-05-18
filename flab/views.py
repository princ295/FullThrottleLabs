from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.reverse import reverse

from .models import ActivityPeriod
from .serializers import ActivityPeriodSerializer


class ActivityListView(generics.ListAPIView):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer
    name = "activity-list"
    

class ActivityDetalsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer
    name = "activityperiod-detail"
