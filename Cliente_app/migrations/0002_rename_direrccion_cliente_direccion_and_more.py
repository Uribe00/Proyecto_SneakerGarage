# Generated by Django 5.1.1 on 2024-11-27 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='direrccion',
            new_name='direccion',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=15),
        ),
    ]