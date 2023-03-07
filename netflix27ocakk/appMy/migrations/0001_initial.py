# Generated by Django 4.1.5 on 2023-03-05 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Kategoi')),
            ],
        ),
        migrations.CreateModel(
            name='Diziler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Dizi Adı')),
                ('text', models.TextField(max_length=500, verbose_name='Açıklama')),
                ('image', models.ImageField(upload_to='diziler', verbose_name='Dizi Resmi')),
                ('date_now', models.DateField(verbose_name='Yapım Tarihi')),
            ],
        ),
        migrations.CreateModel(
            name='Filimler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Dizi Adı')),
                ('text', models.TextField(max_length=500, verbose_name='Açıklama')),
                ('image', models.ImageField(upload_to='diziler', verbose_name='Dizi Resmi')),
                ('date_now', models.DateField(verbose_name='Yapım Tarihi')),
            ],
        ),
        migrations.CreateModel(
            name='Populer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Dizi Adı')),
                ('text', models.TextField(max_length=500, verbose_name='Açıklama')),
                ('image', models.ImageField(upload_to='diziler', verbose_name='Dizi Resmi')),
                ('date_now', models.DateField(verbose_name='Yapım Tarihi')),
            ],
        ),
    ]
