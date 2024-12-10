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

    def eliminar_producto(self, nombre):
        # Eliminar un producto del inventario
        for i, producto in enumerate(self.productos):
            if producto.nombre == nombre:
                del self.productos[i]
                print(f"Producto {nombre} eliminado correctamente.")
                return
        print(f"Producto {nombre} no encontrado.")
