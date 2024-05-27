# Generated by Django 5.0.4 on 2024-05-25 00:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miAplicacion', '0002_rename_estado_pedido_descripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='Descripcion',
            new_name='descripcion',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.proveedor'),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='producto',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.producto'),
        ),
        migrations.AlterField(
            model_name='detallefactura',
            name='producto',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.producto'),
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='producto',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.producto'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='cliente',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.cliente'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='proveedor',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.proveedor'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.proveedor'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='direccion',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='venta',
            name='cliente',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.cliente'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='factura',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.factura'),
        ),
        migrations.AlterField(
            model_name='ventasproducto',
            name='producto',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.producto'),
        ),
    ]
