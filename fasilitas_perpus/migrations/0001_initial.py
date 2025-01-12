# Generated by Django 5.0.2 on 2024-03-20 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anggota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('alamat', models.TextField()),
                ('nomor_telepon', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('pengarang', models.CharField(max_length=100)),
                ('penerbit', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RakBuku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Peminjaman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_pinjam', models.DateField()),
                ('tanggal_kembali', models.DateField(blank=True, null=True)),
                ('anggota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fasilitas_perpus.anggota')),
                ('buku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fasilitas_perpus.buku')),
            ],
        ),
    ]
