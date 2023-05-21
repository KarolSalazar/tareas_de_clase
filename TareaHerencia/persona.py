class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def __str__(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}"
    
    def edad_retiro(self, años):
        return self._edad + años
