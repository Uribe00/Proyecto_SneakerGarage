# Generated by Django 5.1.3 on 2024-11-29 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proveedores_app', '0002_remove_proveedor_lote_proveedor_direccion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='fecha_ultimo_envio',
            field=models.DateField(default='2024-01-01'),
            preserve_default=False,
        ),
    ]
