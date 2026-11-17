
class Estacionamiento:
    def __init__(self, horas):
        self.horas = horas

    def calcularPago(self):
        if 1 <= self.horas <= 2:
            return self.horas * 15.00
        elif 3 <= self.horas <= 5:
            return self.horas * 12.00
        elif self.horas > 5:
            return self.horas * 10.00
        else:
            return 0

    def mostrarRecibo(self):
        total = self.calcularPago()
        print(f"Horas: {self.horas}")
        print(f"Importe: ${total:.2f}")


horas = int(input("Ingrese las horas de estacionamiento: "))
if horas > 0:
    estacionamiento = Estacionamiento(horas)
    estacionamiento.mostrarRecibo()
else:
    print("Por favor, ingrese un número entero mayor que cero.")

#¿Como puedo correr este programa en la terminal?, por ejemplo (python main_1.py)
#Para correr este programa en la terminal, sigue estos pasos:
#1. Asegúrate de tener Python instalado en tu sistema. Puedes verificarlo ejecutando `python --version` o `python3 --version` en la terminal.
#2. Guarda el código en un archivo llamado `main_1.py`.
#3. Abre la terminal y navega hasta el directorio donde guardaste `main_1.py`.
#4. Ejecuta el programa con el siguiente comando:
#   ```
#   python main_1.py
#   ```
#   o
#   ```
#   python3 main_1.py
#   ```