from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [

    path('', views.page_not_found, name='page_not_found'),
]
