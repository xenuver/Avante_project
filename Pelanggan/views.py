from django.shortcuts import render
from .models import Customer


def home(request):
    context = {
    }
    return render(request,'index.html',context)


    
def daftar_pelanggan(request):
    pelanggan = Pelanggan.objects.all()
    return render(request, 'daftar_pelanggan.html',{'pelanggan': pelanggan})