from django.shortcuts import render
from django.http import  HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json

DB = settings.DB_FILE

from db import readDB,writeDB

# Create your views here.
@csrf_exempt
def funMen(request):
    if request.method == "GET":
        data = readDB(filename = DB)
        req = data['database']["men"]

        res = {'men' : req}

        return JsonResponse(res)

    elif request.method == "POST":

        dicObj = json.loads(request.body)
        if (dicObj['add'] == 'true'):
            o = dicObj['obj']
            writeDB(obj=o,loc='men', filename=DB)
            

        return JsonResponse({"request" : "posted in men section"})

    
@csrf_exempt
def funWomen(request):
    if request.method == "GET":
        data = readDB(filename=DB)
        req = data['database']["women"]

        res = {'women' : req}

        return JsonResponse(res)

    elif request.method == "POST":

        dicObj = json.loads(request.body)
        if (dicObj['add'] == 'true'):
            o = dicObj['obj']
            writeDB(obj=o, loc='women',filename=DB)
            

        return JsonResponse({"request" : "posted in women section"})


def helloworld(request):
    return HttpResponse("<h1> hello world </h1>")