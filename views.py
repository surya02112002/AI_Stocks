from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))
def login(request):
    template =loader.get_template("login.html")
    return HttpResponse(template.render({},request))
def alluser(request):
    return render(request,"homelogin.html")
def rethome(request):
    return render(request,"index.html")