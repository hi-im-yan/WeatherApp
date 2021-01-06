from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail_info/<str:pk>', views.detail, name='detail_info')
]
