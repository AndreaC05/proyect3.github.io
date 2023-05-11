from Interface import InterfaceVista
from ArchivoClaseAuto import ClaseCamion
class ClaseVistaCamion(InterfaceVista):
    def mostrar_datos(self,camion):
        print(f"Tipo    : {camion.tipo}")
        print(f"Marca   : {camion.marca}")
        print(f"Color   : {camion.color}")
        print(f"Precio  : {camion.precio}")
        print(f"Cantidad: {camion.cantidad}")


    def iniciar_proceso(self):
        mi_camion = ClaseCamion("Camión", "Mitsubishi", "Rojo y Blanco", 121237, 3)
        self.mostrar_datos(mi_camion)
        
