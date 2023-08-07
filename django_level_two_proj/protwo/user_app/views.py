from django.shortcuts import render
from django.http import HttpResponse
from user_app.models import Users
# Create your views here.
def index(request):
    users_list = Users.objects.order_by('first_name')
    user_dict = {"users_record": users_list}
    return render(request,"user_app/index.html",context=user_dict)

# Create your views here.
