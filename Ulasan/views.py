from django.shortcuts import render
from .models import Review


def daftar_review(request):
    review = review.objects.all()
    return render(request, 'daftar_review.html', {'review': review})

def home(request):
    context = {
    }
    return render(request,'index.html',context)