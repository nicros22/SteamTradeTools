from django.urls import path, include

from .views import *

app_name = 'interface'

urlpatterns = [
    path('parser/', include("parser.urls")),
]