from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {"insert_me": "Sudam Wanve"}
    return render(request,"first_app/index.html",context=my_dict)
def help(request):
    my_name = {"user_name": "Sudam Wanve"}
    return render(request,"first_app/help.html",context=my_name)

def gallery(request):
    return render(request,"first_app/gallery.html")
