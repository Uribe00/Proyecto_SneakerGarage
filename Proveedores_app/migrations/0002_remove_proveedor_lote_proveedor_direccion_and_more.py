# Generated by Django 5.1.3 on 2024-11-29 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proveedores_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='lote',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='direccion',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='email',
            field=models.EmailField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='id_proveedor',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
