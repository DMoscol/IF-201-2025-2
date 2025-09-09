from empresa import Empresa
from empleado_tiempo_completo import EmpleadoTiempoCompleto
from empleado_por_horas import EmpleadoPorHoras


empresa = Empresa('URP Tech')
    
    # Crear empleados
emp1 = EmpleadoTiempoCompleto('Juan Perez', 3000, 500)
emp1.mostrar_informacion()
emp2 = EmpleadoPorHoras('Ana Torres', 2000, 40)
emp2.mostrar_informacion()
    
    
# Pagar
empresa.pagar_empleado(emp1)
empresa.pagar_empleado(emp2, 30)