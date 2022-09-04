from django.shortcuts import render
from django. http import HttpResponse, JsonResponse
from .models import detail

# Create your views here.

def index(request):
    return render(request, 'index.html')

def getDetails(request, key):
    try:
        response = detail.objects.get(key = key)
        return JsonResponse({
            "status" : "success",
            "message" : response.value
        })

    except Exception as e:
        return JsonResponse({
            "status" : "error",
            "message" : str(e)
        })

