from django.db import models

# Create your models here.
class ActivityPeriod(models.Model):
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)

class Period(models.Model):
    ref = models.ForeignKey(ActivityPeriod , related_name="activity_periods", on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=False)
    end_time = models.DateTimeField(auto_now_add=False)
