from ArchivoVehiculo2 import ClaseVehiculo
class MetaClaseMoto(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        if '__init__' in attrs:
            init = attrs['__init__']
            if hasattr(init, '__annotations__'):
                annotations = init.__annotations__
                if 'cantidad' not in annotations:
                    raise TypeError("El atributo 'cantidad' debe ser definido.")
        return super().__init__(name, bases, attrs)
         

class ClaseMoto(ClaseVehiculo, metaclass = MetaClaseMoto):
    def __init__(self, tipo, marca, color, precio, cantidad):

        super().__init__(tipo, marca, color, precio, cantidad)




