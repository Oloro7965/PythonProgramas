class quadrado:
    def __init__(self, lado):
        self.lado = lado
    def get_lado(self):
        return self.lado
    def set_lado(self,lado_novo):
        self.lado=lado_novo
    def calcular_area(self):
        return self.lado**2
q1 = quadrado(4)
print(q1.get_lado())
print(q1.calcular_area())
q1.set_lado(7)
print(q1.get_lado())
print(q1.calcular_area())

