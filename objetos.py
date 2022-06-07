# Python es un lenguaje orientado a objetos
# Casi todo en Python es un objeto
# Una clase es un modelo o patrón del cual se pueden crear múltiples objetos
# Una clase es un plantilla, que define propiedades o atributos (variables) y 
# métodos (funciones)
# Hay que declarar o crear una clase antes de poder crar objetos e esa clase
# Al crear un objeto de una clase, es lo mismo que decir "se crea una instancia
# de la clase"

# crear una clase
class Persona:
    def crear(self, nombreP:str):
        self.nombre = nombreP
        
    def mostrar(self):
        print(self.nombre)
        
# programa principal
# crear una instancia de la clase Persona
persona1 = Persona()
print(type(persona1))
persona1.crear('Pedro')
persona1.mostrar()

persona2 = Persona()
persona2.crear('Mery')
persona2.mostrar()

# método __init__
# Es un método especial, su principal objetivo es inicializar propiedades del 
# objeto que se instancia
# El método __init__ se ejecuta cuando se crea el objeto
# Este método no retorna datos
# Este método recibe parámetros para iniciaizar atributos del objeto

class Estudiante:
    def __init__(self):
        self.nombre = input('Ingrese el nombre del estudiante:\n')
        self.nota= int(input('Ingrese la nota final del estudiante:\n'))

    def imprimir(self):
        print("Nombre:", self.nombre) 
        print("Nota:", self.nota) 
    
    def aprobar(self):
        if self.nota >= 3:
            print('Aprobó')
        else:
            print('No aprobó')
        
estudiante1 = Estudiante()
estudiante1.imprimir()
estudiante1.aprobar()
              
        