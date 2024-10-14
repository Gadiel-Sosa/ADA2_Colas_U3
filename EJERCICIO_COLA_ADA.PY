from collections import deque

class Cola:
    def __init__(self):
        self.elementos = deque()
        
    def encolar(self, valor):
        self.elementos.append(valor)
        
    def desencolar(self):
        return self.elementos.popleft()
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def tamaño(self):
        return len(self.elementos)
    
    def mostrar(self):
        for elemento in self.elementos:
            print(elemento, end=" ")
        print() 
        
def sumar_colas(cola_a, cola_b):
    cola_resultante = Cola()
    
    while not cola_a.esta_vacia() and not cola_b.esta_vacia():
        valor_a = cola_a.desencolar()
        valor_b = cola_b.desencolar()
        cola_resultante.encolar(valor_a + valor_b)
    return cola_resultante

cola_a = Cola()
cola_b = Cola()

cola_a.encolar(3)
cola_a.encolar(4)
cola_a.encolar(2)
cola_a.encolar(8)
cola_a.encolar(12)

cola_b.encolar(6)
cola_b.encolar(2)
cola_b.encolar(9)
cola_b.encolar(11)
cola_b.encolar(3)

print("Cola A:")
cola_a.mostrar()

print("Cola B:")
cola_b.mostrar()

cola_resultado = sumar_colas(cola_a, cola_b)

print("Cola Resultado:")
cola_resultado.mostrar()

    
            