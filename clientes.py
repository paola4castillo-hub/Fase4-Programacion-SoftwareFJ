# Clase Cliente

class Cliente:

    def __init__(self, nombre, correo):

        if nombre == "":
            raise ValueError("El nombre no puede estar vacío")

        if "@" not in correo:
            raise ValueError("Correo inválido")

        self.__nombre = nombre
        self.__correo = correo

    def mostrar_datos(self):

        return f"Cliente: {self.__nombre} - Correo: {self.__correo}"
