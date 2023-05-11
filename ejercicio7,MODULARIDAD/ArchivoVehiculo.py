class ClaseVehiculo:
    def __init__(self, tipo, marca, color, precio, cantidad):

        self.tipo = tipo
        self.marca = marca
        self.color = color
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_informacion(self):

        print(f"Tipo    : {self.tipo}")
        print(f"Marca   : {self.marca}")
        print(f"Color   : {self.color}")
        print(f"Precio  : {self.precio}")
        print(f"Cantidad: {self.cantidad}")
