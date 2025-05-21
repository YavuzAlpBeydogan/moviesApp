from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategori Adı")

class Movie(models.Model):
    film_adi = models.CharField(max_length=200, verbose_name="Film Adı")
    aciklama = models.TextField(verbose_name="Açıklama")
    resim = models.CharField(max_length=200, verbose_name="Resim")
    anasayfa = models.BooleanField(default=False, verbose_name="Anasayfada Göster")
