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

    def agregar_producto(self, nombre, precio, cantidad):
        # Agregar un nuevo producto a la lista
        producto = ProductoAlimenticio(nombre, precio, cantidad)
        self.productos.append(producto)
        print(f"Producto {nombre} agregado correctamente.")

    def listar_productos(self):
        # Mostrar todos los productos en el inventario
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            print("Productos en el inventario:")
            for producto in self.productos:
                print(producto)    
