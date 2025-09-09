class Empresa:
    def __init__(self, nombre: str):
        self.nombre = nombre
        
    def pagar_empleado(self, empleado, horas: int = 0):
        """ Aplica polimorfismo: aceptar cualquier tipo de empleado """
        if horas > 0:
            print(f'Pagando a empleado {empleado.nombre} | Salario calculado {empleado.calcular_salario(horas)}')
        else:    
            print(f'Pagando a empleado {empleado.nombre} | Salario calculado {empleado.calcular_salario()}')
        