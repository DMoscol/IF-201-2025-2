import unittest 
class Vehiculo:
    def __init__(self, marca:str, modelo:str):
        self.marca = marca
        self.modelo = modelo
        
    def mostrar_info(self) -> str:
        return f'Datos del vehiculo\n Marca: {self.marca}\n Modelo: {self.modelo}'
    
class Automovil(Vehiculo):
    def __init__(self, marca:str, modelo:str, num_puertas: int):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas
    
    def es_deportivo(self) -> bool:
        return self.num_puertas == 2

#Prueba Unitaria
class TestPruebaAutomovil(unittest.TestCase):
    def setUp(self):
        self.auto1 = Automovil('Mazda', '3', 4)
        self.auto2 = Automovil('Ferrari', '2', 4)
        
    def test_auto_no_deportivo(self):
        self.assertFalse(self.auto1.es_deportivo())
        
    def test_auto_es_deportivo(self):
        self.assertTrue(self.auto2.es_deportivo())

    def test_auto_deportivo_2(self):
        self.assertEqual(self.auto2.es_deportivo() True)
        
    def test_auto_deortivo_3(self):
        self.assertLess()
if __name__ == "__main__":
    unittest.main()