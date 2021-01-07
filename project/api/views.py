from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import InfoSerializer
from .models import Info

import requests
import json
# Create your views here.
api_key = 'e16233c6d2ae48d05006b3bfadef3a81'


@api_view(['GET'])
def urls(request):
    context = {
        "Create Info": "create_info/",
        "List Infos": "list_info/",
        "Detail Info": "detail_info/",
    }
    return Response(context)


@api_view(['GET'])
def listInfos(request):
    infos = Info.objects.all().order_by('name')
    serializer = InfoSerializer(infos, many=True)

    all_id = []
    for serial in serializer.data:
        serial = json.loads(json.dumps(serial))
        dict = {"id": str(serial['id'])}
        all_id.append(dict)

    a = requests.post(
        'http://127.0.0.1:8000/api/update_info', json=all_id)
    return Response(serializer.data)


@api_view(['POST'])
def createInfo(request):
    form_result = request.data
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' +
                       form_result['name'] + '&units=metric&appid=' + api_key + '&lang=pt')

    # Checa se ja existe o CEP pedido no banco de dados
    res = res.json()
    try:
        info = Info.objects.get(id=res['id'])
    except Exception:
        infoData = {
            'id': res['id'],
            'weather': res['weather'][0]['main'],
            'description': res['weather'][0]['description'],
            'icon': res['weather'][0]['icon'],
            'temperature': res['main']['temp'],
            'feels_like': res['main']['feels_like'],
            'temp_min': res['main']['temp_min'],
            'temp_max': res['main']['temp_max'],
            'humidity': res['main']['humidity'],
            'country': res['sys']['country'],
            'name': res['name']
        }

        serializer = InfoSerializer(data=infoData)

        if serializer.is_valid():
            serializer.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@api_view(['GET'])
def detailInfo(request, pk):
    info = Info.objects.get(id=pk)
    serializer = InfoSerializer(instance=info, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def updateInfo(request):
    list_id = []
    for data in request.data:
        list_id.append(data['id'])

    list_str = ','.join(list_id)

    res = requests.get('http://api.openweathermap.org/data/2.5/group?id=' +
                       list_str + '&units=metric&appid=' + api_key + '&lang=pt')
    res = res.json()

    for data in res['list']:
        infoData = {
            'id': data['id'],
            'weather': data['weather'][0]['main'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'temp_min': data['main']['temp_min'],
            'temp_max': data['main']['temp_max'],
            'humidity': data['main']['humidity'],
            'country': data['sys']['country'],
            'name': data['name']
        }
        info = Info.objects.get(id=data['id'])
        serializer = InfoSerializer(instance=info, data=infoData)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)


@api_view(['DELETE', 'POST'])
def deleteInfo(request, pk):
    info = Info.objects.get(id=pk)
    info.delete()
    return HttpResponseRedirect('http://127.0.0.1:8000/')
