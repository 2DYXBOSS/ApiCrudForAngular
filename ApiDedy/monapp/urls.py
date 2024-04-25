from django.contrib import admin
from django.urls import include, path

from monapp.views import Apilist,Apiunique

urlpatterns = [
    path('admin/', admin.site.urls),
    path('grand/',Apilist.as_view() , name='Apilist'),
    path('Apiuni/<int:pk>/',Apiunique.as_view() , name='Apiunique')
]