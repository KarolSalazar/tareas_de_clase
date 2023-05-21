from persona import Persona 
from scipy import stats

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self._salario = salario
        self._responsabilidades_diarias = [] # Lista vacía para almacenar responsabilidades_diarias
        self._cargos = {} # Diccionario vacío para almacenar cargos y responsabilidades_diarias
        

    def presentación(self):
        super().__str__()
        return f"salario: {self._salario}"

    def edad_retiro(self, años):
        nueva_edad = super().edad_retiro(años)
        return f"Edad de retiro: {nueva_edad}"

    def agregar_responsabilidad(self, responsabilidad_diaria):
        self._responsabilidades_diarias.append(responsabilidad_diaria)

    def agregar_cargo(self, cargo, responsabilidad_diaria):
        self._cargos[cargo] = responsabilidad_diaria

    def agregar_responsabilidad_aleatoria(self):
        responsabilidad_aleatoria = int(stats.norm.rvs(loc=70, scale=10))
        self.agregar_responsabilidad(responsabilidad_aleatoria)