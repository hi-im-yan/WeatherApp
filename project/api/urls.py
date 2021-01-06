from django.urls import path

from . import views

urlpatterns = [
    path('', views.urls, name='urls'),
    path('list_infos', views.listInfos, name='list_infos'),
    path('create_info', views.createInfo, name='create_info'),
    path('detail_info/<str:pk>', views.detailInfo, name='detail_info'),
    path('update_info', views.updateInfo, name='update_info'),
]
