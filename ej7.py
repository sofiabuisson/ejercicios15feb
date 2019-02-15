class Empleado():
    def __init__(self, nombre, salario, edad, estudios):
        self.nombre = nombre
        self.salario = salario
        self.edad = edad
        self.estudios = estudios
    def get_nombre(self):
        return self.nombre
    def get_salario(self):
        return self.salario
    def get_edad(self):
        return self.edad
    def get_estudios(self):
        return self.estudios
   
empleado1 = Empleado('Agustin', 4500, 32, 'Informática')
print('El empleado del mes se llama', empleado1.get_nombre(),', su salario es de', empleado1.get_salario(), 'euros, tiene', empleado1.get_edad(), 'años, y estudió', empleado1.get_estudios())
