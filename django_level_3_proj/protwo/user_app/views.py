from django.shortcuts import render
from django.http import HttpResponse
#from user_app.models import Users
from user_app.forms import NewUserForm
# Create your views here.
def index(request):
    return render(request,"user_app/index.html")

# Create your views here.
def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("FORM INVALID")

    return render(request,"user_app/users.html",{'form':form})

