from empleado import Empleado

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre: str, salario_base: float,  tarifa_hora: float):
        super().__init__(nombre, salario_base)
        self.tarifa_hora = tarifa_hora
        
    def calcular_salario(self, horas: int) -> float:
        return super().calcular_salario() + (horas  * self.tarifa_hora)
                
if __name__ == '__main__':
    emp = EmpleadoPorHoras('Ana', 2000, 40)
    print(f'Para la empleada {emp.nombre}:\n El salario calculado es {emp.calcular_salario(30)}')
    # muestre el salario calculado si además trabajó 10 horas normales y 10 horas extras.
    emp.mostrar_informacion()