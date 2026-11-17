class Producto(object):
    def __init__(self, nombre, precio): 
        self.nombre = nombre 
        self.precio = precio 
        self.total = 0 

    def calcular_total(self, cantidad):
        self.total = self.precio * cantidad
       

    def mostrar_total(self):
        print(f"Producto: {self.nombre}") 
        print(f"Total: ${self.total:.2f}") 


producto1 = Producto("Cuaderno", 35) 
producto1.calcular_total(3) 
producto1.mostrar_total()

#1. ¿Cuál es el nombre de la clase? 
# - Producto
#2. ¿Cuáles son sus propiedades? 
# - nombre
# - precio
# - total
#3. ¿Cuáles son sus métodos? 
# - calcular_total
# - mostrar_total
#4. ¿Qué función cumple __init__? 
# - Es el constructor de la clase, se utiliza para inicializar las propiedades del objeto cuando se crea una instancia de la clase.
#5. ¿Para qué se utiliza self? 
# - Se utiliza para hacer referencia a las propiedades y métodos del objeto actual dentro de la clase.
#6. ¿En qué instrucción se crea un objeto? 
# - en la de producto1 = Producto(cuaderno, 35)
#7. ¿Cuál es el nombre del objeto? 
# - producto1
#8. ¿Cómo se llama a calcular_total()? 
# - producto1.calcular_total(3)
#9. ¿Qué valores recibe el constructor cuando se crea el objeto? 
# - "Cuaderno" y 35
#10. ¿Qué resultado mostrará el programa? 
# - Producto: Cuaderno

class Rectangulo(object):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        # COMPLETAR: guardar las propiedades

    def calcular_area(self):
        return self.base * self.altura
        
        # COMPLETAR: regresar el área pass

    def mostrar_area(self):
        print(f"Base: {self.base}")
        print(f"Altura: {self.altura}")
        print(f"Área: {self.calcular_area()}")

rectangulo1 = Rectangulo(8,5)
rectangulo1.mostrar_area()

# COMPLETAR: crear un objeto con base 8 y altura 5 
# COMPLETAR: llamar al método para mostrar el área 


class Operacion(object): 
     def __init__(self, numero1, numero2):
        self.numero1 = numero1 
        self.numero2 = numero2

    def calcular(self): 
        return self.numero1 + self.numero2

class Multiplicacion(Operacion): 
    def calcular(self): 
        return self.numero1 * self.numero2 

operacion1 = Operacion(8, 4) 
operacion2 = Multiplicacion(8, 4) 
print(operacion1.calcular()) 
print(operacion2.calcular()) 

#1. ¿Cuál es la clase padre?
# - Operacion 
#2. ¿Cuál es la clase hija? 
# - Multiplicacion
#3. ¿Cómo se indica la herencia? 
# - poniendo el nombre de la clase entre parentesisis
#4. ¿Qué propiedades utiliza la clase hija? 
# - numero1
# - numero2
#5. ¿Por qué puede utilizarlas sin definir su propio __init__? 
# - porque lo hereda de la clase padre
#6. ¿Por qué los métodos calcular() tienen resultados distintos? 
# - porque cada uno tiene su propio metodo para calcular
#7. ¿Qué valores se imprimen? 
# - 12
# - 32
#8. ¿Qué sucedería si eliminamos calcular() de Multiplicacion?
# - Se utilizaría el método calcular() de la clase padre, que realiza la suma en lugar de la multiplicación.