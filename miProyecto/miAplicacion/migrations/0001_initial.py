# Generated by Django 5.0.4 on 2024-05-22 17:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=100)),
                ('documento', models.CharField(max_length=50)),
                ('direccion', models.CharField(default='', max_length=200)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(default=None, max_length=100, null=True)),
                ('codigo', models.CharField(default=None, max_length=50, null=True)),
                ('marca', models.CharField(default=None, max_length=50, null=True)),
                ('precio_unidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.IntegerField()),
                ('stock', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo_producto', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(default='', max_length=254)),
                ('direccion', models.CharField(default='', max_length=200)),
                ('provincia', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('importe_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='miAplicacion.pedido')),
                ('producto', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('medio_pago', models.CharField(choices=[('EF', 'Efectivo'), ('TC', 'Tarjeta de Crédito'), ('TD', 'Tarjeta de Débito'), ('TR', 'Transferencia')], max_length=2)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='miAplicacion.factura')),
                ('producto', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='miAplicacion.compra')),
                ('producto', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.proveedor'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='proveedor',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.proveedor'),
        ),
        migrations.AddField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.proveedor'),
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.cliente')),
                ('factura', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.factura')),
            ],
        ),
        migrations.CreateModel(
            name='VentasProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('producto', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventas', to='miAplicacion.venta')),
            ],
        ),
    ]
