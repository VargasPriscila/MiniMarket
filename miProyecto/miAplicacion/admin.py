from django.contrib import admin
from .models import Proveedor, Producto, Cliente, Venta, VentasProducto, Factura, DetalleFactura, Compra, DetalleCompra, Pedido, DetallePedido

class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_producto', 'telefono', 'email', 'direccion', 'provincia')
    search_fields = ('nombre', 'tipo_producto')

class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'codigo', 'marca', 'precio_unidad', 'cantidad', 'stock', 'proveedor')
    search_fields = ('nombre', 'codigo')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'documento', 'direccion', 'telefono', 'email')
    search_fields = ('nombre', 'apellido', 'documento', 'email')

class VentasProductosInline(admin.TabularInline):
    model = VentasProducto

class VentasAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'factura', 'cliente', 'total')
    inlines = [VentasProductosInline]

class DetallesFacturasInline(admin.TabularInline):
    model = DetalleFactura

class FacturasAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'importe_total', 'cliente')
    inlines = [DetallesFacturasInline]

class DetallesComprasInline(admin.TabularInline):
    model = DetalleCompra

class ComprasAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'proveedor', 'total')
    inlines = [DetallesComprasInline]

class DetallesPedidosInline(admin.TabularInline):
    model = DetallePedido

class PedidosAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'proveedor', 'descripcion')
    inlines = [DetallesPedidosInline]

admin.site.register(Proveedor, ProveedoresAdmin)
admin.site.register(Producto, ProductosAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Venta, VentasAdmin)
admin.site.register(Factura, FacturasAdmin)
admin.site.register(Compra, ComprasAdmin)
admin.site.register(Pedido, PedidosAdmin)