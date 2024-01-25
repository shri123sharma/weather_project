# Import necessary modules and functions from Django
from django.contrib import admin
from django.urls import path, include
from .views import forecast, index

# Define the URL patterns for the weather app
urlpatterns = [
    # Default index route pointing to the 'index' view function
    path('', index, name="index"),
    # Route for the 'forecast' view function
    path('updates', forecast, name="forecast")

]
