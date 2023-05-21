from persona import Persona
from empleado import Empleado

empleado1 = Empleado("Paco", 22, 2800000)
empleado1.agregar_responsabilidad(2)
empleado1.agregar_responsabilidad(3)
empleado1.agregar_cargo("Entregas", 2)
empleado1.agregar_cargo("Inventario", 3)
empleado1.agregar_responsabilidad_aleatoria()

print(empleado1) # Nombre: Paco, Edad: 22
print(empleado1.edad_retiro(40)) # Edad de retiro: 62
print(empleado1.presentación()) # Salario: 2800000
print(empleado1._responsabilidades_diarias) # [2, 3, responsabilidad aleatoria]
print(empleado1._cargos) # {'Entregas': 2, 'Inventario': 3}