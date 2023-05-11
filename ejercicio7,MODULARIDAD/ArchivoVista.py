from ArchivoMoto import ClaseMoto

class ClaseVista:
    def iniciar_proceso(self):
        mi_vehiculo2 = ClaseMoto("Moto", "Nexus", "Azul", 4718, 7)
        print(mi_vehiculo2.tipo)
        print(mi_vehiculo2.marca)
        print(mi_vehiculo2.color)
        print(mi_vehiculo2.precio)
        print(mi_vehiculo2.cantidad)
