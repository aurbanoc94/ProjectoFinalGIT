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

    def eliminar_producto(self, nombre):
        # Eliminar un producto del inventario
        for i, producto in enumerate(self.productos):
            if producto.nombre == nombre:
                del self.productos[i]
                print(f"Producto {nombre} eliminado correctamente.")
                return
        print(f"Producto {nombre} no encontrado.")
