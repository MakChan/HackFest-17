from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import RegForm
# Create your views here.
def index(request):
    return render(request, 'org/home.html')

def blog(request):
    return render(request, 'org/blog.html')

def cases(request):
    return render(request, 'org/cases.html')

def register(request):
    if request.method == POST:
        form = RegForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/Thanks for registering/')
    else:
        form = RegForm()

    return render(request,'register.html', {'form':form})
