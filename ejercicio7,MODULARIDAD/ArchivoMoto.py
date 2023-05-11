from ArchivoVehiculo import ClaseVehiculo

class ClaseMoto(ClaseVehiculo):

    def __init__(self, tipo, marca, color, precio, cantidad):

        super().__init__(tipo, marca, color, precio, cantidad)
