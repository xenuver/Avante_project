from django.shortcuts import render
from .models import Shipping


def home(request):
    context = {
    }
    return render(request,'index.html',context)
    
def daftar_Shipping(request):
    Shipping = Shipping.objects.all()
    return render(request, 'daftar_Shipping.html',{'Shipping': Shipping})
