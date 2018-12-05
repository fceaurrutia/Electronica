# Generated by Django 2.1.3 on 2018-12-05 06:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicativo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_boleta',
            name='total',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detalle_boleta',
            name='cantidad',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='porcentaje',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Porcentaje de Descuento'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fotito',
            field=models.ImageField(upload_to='productos'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_base',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_final',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='tienda',
            name='telefono',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999999999)], verbose_name='Número de Teléfono'),
        ),
    ]
