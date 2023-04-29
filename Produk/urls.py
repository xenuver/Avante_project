from django.urls import path
from . import *
from . import views

urlpatterns = [
    path('cari-produk/', views.cari_produk, name='cari_produk'),
    path('produk/<int:id_produk>/', views.detail_produk, name='detail_produk'),
    path('checkout/', views.checkout, name='checkout'),
    path('proses_checkout/',views.proses_checkout, name='proses_checkout'),
    path('',views.home),
]