from collections import deque

class Cola_Servicios:
    def __init__(self):
        self.cola = deque()

    def agregar_cliente(self, codigo_cliente):
        self.cola.append(codigo_cliente)
        return codigo_cliente

    def atender_cliente(self):
        if self.cola:
            return self.cola.popleft()
        else:
            return 'No hay clientes en la cola'

    def mostrar_cola(self):
        if not self.cola:
            print("No hay clientes en la cola.")
        else:
            print("Clientes en la cola:", list(self.cola))

class SistemaColas:
    def __init__(self):
        self.colas = {
            1: Cola_Servicios(),
            2: Cola_Servicios(),
            3: Cola_Servicios()
        }
        self.contador = 0  

    def generar_codigo_cliente(self):
        self.contador += 1
        return f"C{self.contador}"

    def manejar_entrada(self, entrada):
        try:
            comando, servicio = entrada.split()
            servicio = int(servicio)

            if servicio not in self.colas:
                print(f"Error: El servicio {servicio} no existe.")
                return

            if comando == 'C':
                codigo_cliente = self.generar_codigo_cliente()
                self.colas[servicio].agregar_cliente(codigo_cliente)
                print(f"Cliente agregado al servicio {servicio}. Código de cliente: {codigo_cliente}")
            elif comando == 'A':
                codigo_cliente = self.colas[servicio].atender_cliente()
                print(f"Atendiendo al cliente del servicio {servicio}. Código de cliente: {codigo_cliente}")
            else:
                print(f"Comando desconocido: {comando}")
            
           
            self.mostrar_estado_colas()

        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar el comando correctamente.")
        except KeyError:
            print("El servicio ingresado no es válido.")

    def mostrar_estado_colas(self):
        print("\nEstado actual de las colas:")
        for servicio, cola in self.colas.items():
            print(f"Servicio {servicio}: ", end="")
            cola.mostrar_cola()

    def mostrar_servicios(self):
        print("\nServicios Disponibles:")
        print('Servicio 1')
        print('Servicio 2')
        print('Servicio 3')

sistema = SistemaColas()

while True:
    sistema.mostrar_servicios()
    entrada = input("Ingrese comando (C para cliente, A para atender o 'salir') y número de servicio: ")
    if entrada.lower() == 'salir':
        break
    sistema.manejar_entrada(entrada)
        
        
        
        
        
    
    
        
            
            
            
        
        
        
        
        
