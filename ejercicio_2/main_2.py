class Operacion:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calcular(self):
        return self.num1 + self.num2

    def mostrarResultado(self):
        resultado = self.calcular()
        print(f"Resultado de la suma: {resultado}")


class Resta(Operacion):
    def calcular(self):
        return self.num1 - self.num2



numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))

suma = Operacion(numero1, numero2)
resta = Resta(numero1, numero2)

suma.mostrarResultado()
resta.mostrarResultado()


