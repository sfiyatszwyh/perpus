from django.db import models

class Buku(models.Model):
    judul = models.CharField(max_length=100)
    pengarang = models.CharField(max_length=100)
    penerbit = models.CharField(max_length=100)

class RakBuku(models.Model):
    nama = models.CharField(max_length=100)

class Peminjaman(models.Model):
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    anggota = models.ForeignKey('Anggota', on_delete=models.CASCADE)
    tanggal_pinjam = models.DateField()
    tanggal_kembali = models.DateField(null=True, blank=True)

class Anggota(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    nomor_telepon = models.CharField(max_length=15)
