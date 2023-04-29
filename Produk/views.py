from django.shortcuts import render
from .models import Product
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, KeranjangBelanja

def home(request):
    context = {
    }
    return render(request,'index.html',context)


    
def daftar_produk(request):
    produk = Produk.objects.all()
    return render(request, 'Produk.html', {'produk': produk})

def cari_produk(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        if query is not None:
            hasil_pencarian = Produk.objects.filter(nama_produk__icontains=query)
            return render(request, 'Produk.html', {'hasil_pencarian': hasil_pencarian, 'query': query})

    return render(request, 'cari_produk.html')

def detail_produk(request, id_produk):
    produk = get_object_or_404(Produk, id=id_produk)
    return render(request, 'Produk.html', {'produk': produk})




def tambah_ke_keranjang(request, id_produk):
    produk = get_object_or_404(Produk, id=id_produk)
    keranjang_belanja, created = KeranjangBelanja.objects.get_or_create(
        user=request.user, produk=produk)
    if not created:
        keranjang_belanja.jumlah += 1
        keranjang_belanja.save()
    return redirect('keranjang')

def keranjang(request):
    keranjang_belanja = KeranjangBelanja.objects.filter(user=request.user)
    total_harga = sum([item.produk.harga_produk * item.jumlah for item in keranjang_belanja])
    return render(request, 'Produk.html', {'keranjang_belanja': keranjang_belanja, 'total_harga': total_harga})




def checkout(request):
    keranjang_belanja = KeranjangBelanja.objects.filter(user=request.user)
    total_harga = sum([item.produk.harga_produk * item.jumlah for item in keranjang_belanja])
    return render(request, 'Produk.html', {'keranjang_belanja': keranjang_belanja, 'total_harga': total_harga})

def proses_checkout(request):
    keranjang_belanja = KeranjangBelanja.objects.filter(user=request.user)
    for item in keranjang_belanja:
        item.delete()
    return redirect('produk')







