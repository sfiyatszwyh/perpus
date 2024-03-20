from django.contrib import admin
from django.urls import path
from fasilitas_perpus import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pinjam-buku/', views.pinjam_buku, name='pinjam_buku'),
    path('', views.pendaftaran_mahasiswa, name='home'),
]
