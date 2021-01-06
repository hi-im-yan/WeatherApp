from django.shortcuts import render

import requests
# Create your views here.

my_api_url = 'http://127.0.0.1:8000/api/'


def home(request):
    res = requests.get(my_api_url + 'list_infos')

    context = {
        "infos": res.json()
    }

    return render(request, 'app/infos.html', context)


def detail(request, pk):
    res = requests.get(my_api_url + 'detail_info/' + pk)
    print(res.json)
    context = {
        "info": res.json()
    }

    return render(request, 'app/detail.html', context)
