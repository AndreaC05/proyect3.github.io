from ArchivoMoto2 import ClaseMoto

class ClaseVistaConError:
    def iniciar_proceso(self):
        mi_moto = ClaseMoto("Moto", "Nexus", "Azul", 4687, 7)
        print(mi_moto.tipo)
        print(mi_moto.marca)
        print(mi_moto.color)
        print(mi_moto.precio)
        print(mi_moto.cantidad)
