from django.urls import path
from .views import *

app_name="core"

urlpatterns = [
    path('',primera_vista,name='primera_vista')
]