# Generated by Django 5.1.3 on 2024-11-29 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos_app', '0004_rename_presio_productos_precio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='lote',
            new_name='marca',
        ),
        migrations.AddField(
            model_name='productos',
            name='modelo',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]