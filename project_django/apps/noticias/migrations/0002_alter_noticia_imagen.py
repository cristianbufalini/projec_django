# Generated by Django 4.2.6 on 2023-11-20 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(upload_to='media.noticias'),
        ),
    ]
