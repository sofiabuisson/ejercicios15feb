class Fraccion():
    def __init__(self, numerador, denominador, numerador2, denominador2):
        self.numerador = numerador
        self.denominador = denominador
        self.numerador2 = numerador2
        self.denominador2 = denominador2
    def suma(self):
        return ((self.numerador / self.denominador) + (self.numerador2 / self.denominador2))
    def resta(self):
        return ((self.numerador / self.denominador) - (self.numerador2 / self.denominador2))
    def multiplica(self):
        return ((self.numerador / self.denominador) * (self.numerador2 / self.denominador2))
    def divide(self):
        return ((self.numerador / self.denominador) / (self.numerador2 / self.denominador2))
   
fraccion = Fraccion(1, 2, 1, 2)
print(fraccion.divide())
