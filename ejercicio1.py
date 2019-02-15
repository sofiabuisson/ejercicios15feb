class Cuenta():
    
    def __init__(self, ingreso,reintegro, transferencia):
        self.ingreso=ingreso
        self.reintegro=reintegro
        self.transferencia=transferencia
    
    def get_ingreso(self):
        return self.ingreso
    
    def get_reintegro(self):
        return self.reintegro
        
    def get_transferencia(self):
        return self.transferencia
    
    def set_ingreso(self, ingreso):
        self.ingreso=ingreso
    
    def set_reintegro(self, reintegro):
        self.reintegro=reintegro
        
    def set_transferencia(self, transferencia):
        self.transferencia=transferencia
    
ingreso=Cuenta(50,100,20)
print(ingreso.get_ingreso())

