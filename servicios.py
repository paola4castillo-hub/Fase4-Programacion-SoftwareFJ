# Clases de servicios

from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self):
        pass


class ReservaSala(Servicio):

    def __init__(self, horas):

        super().__init__("Reserva de Sala")
        self.horas = horas

    def calcular_costo(self):

        return self.horas * 50000


class AlquilerEquipo(Servicio):

    def __init__(self, dias):

        super().__init__("Alquiler de Equipos")
        self.dias = dias

    def calcular_costo(self):

        return self.dias * 30000


class AsesoriaEspecializada(Servicio):

    def __init__(self, horas):

        super().__init__("Asesoría Especializada")
        self.horas = horas

    def calcular_costo(self):

        return self.horas * 80000
