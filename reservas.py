# Clase Reserva

class Reserva:

    def __init__(self, cliente, servicio):

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):

        self.estado = "Confirmada"

    def cancelar(self):

        self.estado = "Cancelada"

    def mostrar_reserva(self):

        return f"""
Cliente: {self.cliente.mostrar_datos()}
Servicio: {self.servicio.nombre}
Costo: ${self.servicio.calcular_costo()}
Estado: {self.estado}
"""
