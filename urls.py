from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login",views.login, name="login"),
    path("alluser",views.alluser,name="alluser"),
    path("rethome",views.rethome, name="rethome"),
]


