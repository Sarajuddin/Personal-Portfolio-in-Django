from django.urls import path
from sarajuapp import views


urlpatterns = [
    path('', views.home)
]