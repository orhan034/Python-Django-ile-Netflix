# Generated by Django 4.1.5 on 2023-03-05 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0003_diziler_imdb_filimler_imdb_populer_imdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='diziler',
            name='tur',
            field=models.CharField(max_length=50, null=True, verbose_name='Filmin Türü'),
        ),
        migrations.AddField(
            model_name='filimler',
            name='tur',
            field=models.CharField(max_length=50, null=True, verbose_name='Filmin Türü'),
        ),
        migrations.AddField(
            model_name='populer',
            name='tur',
            field=models.CharField(max_length=50, null=True, verbose_name='Filmin Türü'),
        ),
    ]
