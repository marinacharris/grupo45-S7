# Herencia, se puede definir una clase que hereda propiedades y m+etodos de 
# otra clase
# Clase principal clase base, es la clase de la que se hereda
# Clase secundaria o derivada, es la clase que hereda de otra clase

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def imprimir(self):
        print(self.nombre,self.apellido)
        
x = Persona('Carlos','Peña')
x.imprimir()

class Estudiante(Persona):
    def saludo(self):
        print(f'Hola {self.nombre}') 

y = Estudiante('Ana', 'Ruíz')
y.imprimir()
y.saludo()