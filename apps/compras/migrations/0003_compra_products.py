# Generated by Django 3.0.8 on 2020-11-19 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
        ('compras', '0002_compra_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='products',
            field=models.ManyToManyField(through='compras.CompraCantidades', to='productos.Producto'),
        ),
    ]
