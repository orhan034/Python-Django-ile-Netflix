from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(("Kategoi"), max_length=50)
    def __str__(self):
       return self.title
   
class Dizilerim(models.Model):
    category  = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE, null=True)
    name = models.CharField(("Dizi Adı"), max_length=50)
    imdb = models.FloatField(("IMDb Oranı"), default=0)
    tur = models.CharField(("Filmin Türü"), max_length=50, null=True)
    text = models.TextField(("Açıklama"), max_length=500)
    image = models.ImageField(("Dizi Resmi"), upload_to='diziler', max_length=None)
    date_now = models.DateField(("Yapım Tarihi"), auto_now_add=False)
 
    def __str__(self):
        return self.name
    
