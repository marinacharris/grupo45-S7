# implemente un a clase llamada Operaciones. Se deben cargar dos valores 
# decimales en el método __init__ y calcular suma, resta multiplicación y division
# cada una con un método

class Operaciones:
    def __init__(self, a:float,b:float):
        self.a = a
        self.b = b
        
    def sum(self):
        suma = self.a + self.b
        print(f'La suma es: {suma}')
    
    def sub(self):
        resta = self.a - self.b
        print(f'La resta es: {resta}')
        
    def mul(self):
        multi = self.a * self.b
        print(f'La multiplicación es: {multi}')
    
    def div(self):
        try:
            division = self.a / self.b
            print(f'La division es {division}')
        except:
            print(f'La division entre cero es inválida')
        
	
operacion1 = Operaciones(8.0,10.2)
operacion1.a = 40
operacion1.b = 20
operacion1.sum()
operacion1.sub()
operacion1.mul()
operacion1.div()