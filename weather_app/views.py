# Import necessary modules
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest
# Import custom utility functions and data
from weather_app.utils import get_weather, context_data
from django.contrib import messages


# View function for handling the 'forecast' page
def forecast(request):
    # Return a simple HTTP response indicating that the forecast is done
    return HttpResponse("done")


def index(request):
    # Check if the request method is POST
    if request.method == "POST":
        # Get the query parameter from the POST data
        query = request.POST.get("query")
        # Get weather data based on the provided query
        data = get_weather(query)
        # Check if the data is a dictionary (indicating a successful weather API response)
        if isinstance(data, dict):
            # Render the 'main.html' template with the weather data
            return render(request, "main.html",  data)
        else:
            # Add an error message and redirect to the 'index.html' template
            messages.error(request, "Invalid data submitted")
            return render(request, "index.html")
        # Render the 'index.html' template (possibly with an error message)
        return render(request, "index.html")
    # Render the 'index.html' template for GET requests
    return render(request, "index.html")