from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import InfoSerializer
from .models import Info

import requests
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
    return Response(serializer.data)


@api_view(['POST'])
def createInfo(request):
    form_result = request.data

    res = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' +
                       form_result['name'] + '&units=metric&appid=' + api_key + '&lang=pt')

    res = res.json()
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

    return Response(serializer.data)


@api_view(['GET'])
def detailInfo(request, pk):
    info = Info.objects.get(id=pk)
    serializer = InfoSerializer(instance=info, many=False)
    return Response(serializer.data)
