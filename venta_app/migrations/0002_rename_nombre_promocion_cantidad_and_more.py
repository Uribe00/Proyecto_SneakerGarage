# Generated by Django 5.1.3 on 2024-11-29 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promocion',
            old_name='nombre',
            new_name='cantidad',
        ),
        migrations.RenameField(
            model_name='promocion',
            old_name='fecha_fin',
            new_name='venta_fecha',
        ),
        migrations.RemoveField(
            model_name='promocion',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='promocion',
            name='fecha_inicio',
        ),
        migrations.RemoveField(
            model_name='promocion',
            name='id_promocion',
        ),
        migrations.RemoveField(
            model_name='promocion',
            name='producto_aplicable',
        ),
        migrations.RemoveField(
            model_name='promocion',
            name='zona_aplicable',
        ),
        migrations.AddField(
            model_name='promocion',
            name='id_ventas',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='promocion',
            name='metodo_pago',
            field=models.CharField(default='default', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='promocion',
            name='precio_total',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]