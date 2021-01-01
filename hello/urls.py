from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("rayyan", views.rayyan, name="rayyan"),
    path("ibrahim", views.ibrahim, name="ibrahim"), 

]