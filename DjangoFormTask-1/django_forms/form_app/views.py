from django.shortcuts import render
from .forms import CustomForm

# Create your views here.


def form(request):
    context={

    }
    return render(request,'form.html',context)

def home(request):
    context={
        'form':CustomForm()
    }
    return render(request,'unsolved.html',context)
