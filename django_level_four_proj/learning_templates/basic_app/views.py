from django.shortcuts import render

# Create your views here.
def index(request):
    context_dic = {'text': 'Hello World', 'number' : 100,'listvar': ['hello','sudam']}
    return render(request,'basic_app/index.html',context=context_dic)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_template.html')

def basic(request):
    return render(request,'basic_app/basic.html')