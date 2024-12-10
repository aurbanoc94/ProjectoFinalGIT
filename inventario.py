class ProductoAlimenticio:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"

class Inventario:
    def __init__(self):
        self.productos = []

    def editar_producto(self, nombre, nuevo_nombre=None, nuevo_precio=None, nueva_cantidad=None):
        # Editar un producto existente
        for producto in self.productos:
            if producto.nombre == nombre:
                if nuevo_nombre:
                    producto.nombre = nuevo_nombre
                if nuevo_precio:
                    producto.precio = nuevo_precio
                if nueva_cantidad:
                    producto.cantidad = nueva_cantidad
                print(f"Producto {nombre} editado correctamente.")
                return
        print(f"Producto {nombre} no encontrado.")