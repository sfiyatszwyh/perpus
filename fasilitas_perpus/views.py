# aplikasi_perpustakaan/views.py
from django.shortcuts import render
from django.http import HttpResponse

def pendaftaran_mahasiswa(request):
    if request.method == 'POST':
        return HttpResponse('Pendaftaran mahasiswa berhasil!')
    else:
        return render(request, 'pendaftaran_mahasiswa.html')

def pinjam_buku(request):
    if request.method == 'POST':
        return HttpResponse('Peminjaman buku berhasil!')
    else:
        return render(request, 'pinjam_buku.html')
