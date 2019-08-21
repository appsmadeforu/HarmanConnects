from django.urls import path

from socialize import views

urlpatterns = [
    path('', views.index, name="index"),
]