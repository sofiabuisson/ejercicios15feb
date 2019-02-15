class Contador():
    def __init__(self, numero):
        self.numero = numero
    def incremento(self):
        return self.numero + 1
    def decremento(self):
        return self.numero - 1
    def get_numero(self):
        return self.numero
    def set_numero(self, numero):
        self.numero = numero

numero = Contador(1)
print(numero.get_numero())
numero.set_numero(3)
print(numero.get_numero())
