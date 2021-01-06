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
