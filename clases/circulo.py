import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

circulo = Circulo(3)

print("Radio:", circulo.radio)
print("Área:", circulo.area())
print("Perímetro:", circulo.perimetro())
