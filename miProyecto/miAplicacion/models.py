from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_producto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(default='', blank=True)
    direccion = models.CharField(max_length=200, default='', blank=True)
    provincia = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, default=None, null=True, blank=True)
    codigo = models.CharField(max_length=50, default=None, null=True, blank=True)
    marca = models.CharField(max_length=50, default=None, null=True, blank=True)
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    stock = models.PositiveIntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, default=None, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200, default='', blank=True)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(default='', blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Factura(models.Model):
    fecha = models.DateField()
    importe_total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, default=None, null=True, blank=True)

    def __str__(self):
        return f"Factura {self.id} - {self.fecha}"

class Venta(models.Model):
    fecha = models.DateField()
    factura = models.ForeignKey(Factura, on_delete=models.PROTECT, default=None, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, default=None, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta {self.id} - {self.fecha}"

class DetalleFactura(models.Model):
    MEDIO_PAGO_CHOICES = [
        ('EF', 'Efectivo'),
        ('TC', 'Tarjeta de Crédito'),
        ('TD', 'Tarjeta de Débito'),
        ('TR', 'Transferencia'),
    ]
    factura = models.ForeignKey(Factura, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, default=None, null=True, blank=True)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    medio_pago = models.CharField(max_length=2, choices=MEDIO_PAGO_CHOICES)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} ({self.get_medio_pago_display()})"

class VentasProducto(models.Model):
    venta = models.ForeignKey(Venta, related_name='ventas', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, default=None, null=True, blank=True)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

class Compra(models.Model):
    fecha = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, default=None, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Compra {self.id} - {self.fecha}"

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, default=None, null=True, blank=True)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

class Pedido(models.Model):
    fecha = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, default=None, null=True, blank=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f"Pedido {self.id} - {self.fecha}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, default=None, null=True, blank=True)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
