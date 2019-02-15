class Libro():
    
    def __init__(self, prestamo, devolucion, dame_info):
        self.prestamo=prestamo
        self.devolucion=devolucion
        self.dame_info=dame_info
    
    def get_prestamo(self):
        return self.prestamo
    
    def get_devolucion(self):
        return self.devolucion
        
    def get_dame_info(self):
        return dame_info
    
    def set_prestamo(self,prestamo):
        self.prestamo=prestamo
    
    def set_devolucion(self, devolucion):
        self.reintegro=reintegro
        
    def set_dame_info(self, dame_info):
        self.dame_info=dame_info
    
prestamo=Libro(43, 5, 'caperucita roja')
print(prestamo.get_prestamo())

