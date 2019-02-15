class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def get_nombre(self):
        return self.nombre
    def get_precio(self):
        return self.precio
class Medicamento(Producto):
    def __init__(self, nombre, precio, compos, porc):
        self.nombre = nombre
        self.precio = precio
        self.compos = compos
        self.porc = porc
    def get_compos(self):
        return self.compos
    def get_porc(self):
        return self.porc
        
class Laboratorio():
    def __init__(self, productos):
         self.productos = productos
     
    def get_nombres(self):
        nombre = []
        for i in range(len(self.productos)):
            medicamento = self.productos[i].get_nombre()
            nombre.append(medicamento)
        return nombre
    def get_precio(self):
        precio = []
        for i in range(len(self.productos)):
            medicamento = self.productos[i].get_precio()
            precio.append(medicamento)
        return precio
    def get_porc(self):
        porc = []
        numro = 0
        for i in range(len(self.productos)-1):
            medicamento = self.productos[i].get_porc()
            porc.append(medicamento)
        return porc
    def get_compos(self):
        compos = []
        for i in range(len(self.productos)-1):
            medicamento = self.productos[i].get_compos()
            compos.append(medicamento)
        return compos
    

prod1 = Medicamento('ibuprofeno', 12, 'h2o', 0.02)
prod2 = Medicamento('couldina', 10, 'NH3', 0.2)
prod3 = Producto('pañales', 20)
productos = []
productos.append(prod1)
productos.append(prod2)
productos.append(prod3)

laboratorio1 = Laboratorio(productos)
print('El laboratorio tiene', laboratorio1.get_nombres(), '\n', 'con sus resepctivos precios', laboratorio1.get_precio(), '\n', 'sus composiciones', laboratorio1.get_compos(), '\n', 'y el porcentaje', laboratorio1.get_porc())
