from django.urls import path
from . import views

app_name = "publicaciones"

urlpatterns = [
    path('', views.index, name="index"),

]