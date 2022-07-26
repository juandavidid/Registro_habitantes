from django.shortcuts import render,HttpResponse
#from .forms import RegistroForm

# Create your views here.

def home(request):
    return render(request,"Appformulario/base.html")


''''


def registro(request):
    data={
        'form':RegistroForm()
    }
    return render(request,'Appformulario/home.html',data)
    

'''

