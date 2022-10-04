from django.contrib import admin
from django.urls import path, include
#from rest_framework import routers
from survey import views

#route = routers.DefaultRouter()

#route.register(r'survey', views.MultipleModels, basename="Survey")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MultipleModels)
]
