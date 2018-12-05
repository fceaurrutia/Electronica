# Generated by Django 2.1.3 on 2018-12-05 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicativo', '0002_auto_20181205_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='boleta',
            name='terminada',
            field=models.BooleanField(default=False, verbose_name='Estado de Venta'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detalle_boleta',
            name='total',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
