from django.shortcuts import render, redirect
from django. http import HttpResponse, JsonResponse
from .models import detail

# Create your views here.

def index(request):
    try:
        x = detail.objects.get(key = "Geography")
        if x:
            return render(request, 'index.html')

    except Exception as e:
        response = redirect('https://indegenous.herokuapp.com/populate')
        return response

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

def populate(request):
    try:
        new_detail = detail(key = "Geography", value = "The Geography of Asgard is dominated by huge mountains.")
        new_detail.save()
        new_detail = detail(key = "History", value = "History of Asgard goes back a millenia.")
        new_detail.save()
        new_detail = detail(key = "Culture", value = "Culturally Asgard remains a mystery to the passer by.")
        new_detail.save()
        new_detail = detail(key = "Language", value = "Language barriers in Asgard do not allow outsiders to live.")
        new_detail.save()
        response = redirect('https://indegenous.herokuapp.com/')
        return response
    except Exception as e:
        return JsonResponse({
            "status" : "error",
            "message" : str(e)
        })