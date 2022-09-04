from django.shortcuts import render, redirect
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

def populate(requet):
    try:
        new_detail = detail(key = "Geography", value = "The Geography of Asgard is dominated by huge mountains.")
        new_detail.save()
        new_detail = detail(key = "History", value = "History of Asgard goes back a millenia.")
        new_detail.save()
        new_detail = detail(key = "Culture", value = "Culturally Asgard remains a mystery to the passer by.")
        new_detail.save()
        new_detail = detail(key = "Language", value = "Language barriers in Asgard do not allow outsiders to live.")
        new_detail.save()
        response = redirect('http://localhost:8000/')
        return response
    except Exception as e:
        return JsonResponse({
            "status" : "error",
            "message" : str(e)
        })