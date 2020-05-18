from django.contrib import admin
from django.urls import path, include
from flab import views

urlpatterns = [
    
    path('v1/api/', views.ActivityListView.as_view(), name=views.ActivityListView.name),
    path('v1/api/<int:pk>', views.ActivityDetalsView.as_view(), name=views.ActivityDetalsView.name),
 
]