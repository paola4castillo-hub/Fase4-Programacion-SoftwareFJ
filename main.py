# Programa principal
    print("Error detectado:", e)
    guardar_log(e)


# OPERACIÓN 6
try:

    cliente6 = Cliente("Sofia", "sofia@gmail.com")
    servicio6 = ReservaSala(5)

    reserva6 = Reserva(cliente6, servicio6)
    reserva6.confirmar()

    print(reserva6.mostrar_reserva())

except Exception as e:

    print("Error:", e)
    guardar_log(e)


# OPERACIÓN 7
try:

    cliente7 = Cliente("Pedro", "pedro@gmail.com")
    servicio7 = AlquilerEquipo(1)

    reserva7 = Reserva(cliente7, servicio7)
    reserva7.cancelar()

    print(reserva7.mostrar_reserva())

except Exception as e:

    print("Error:", e)
    guardar_log(e)


# OPERACIÓN 8
try:

    cliente8 = Cliente("Laura", "laura@gmail.com")
    servicio8 = AsesoriaEspecializada(4)

    reserva8 = Reserva(cliente8, servicio8)
    reserva8.confirmar()

    print(reserva8.mostrar_reserva())

except Exception as e:

    print("Error:", e)
    guardar_log(e)


# OPERACIÓN 9 - ERROR
try:

    cliente9 = Cliente("", "mal")

except Exception as e:

    print("Error detectado:", e)
    guardar_log(e)


# OPERACIÓN 10
try:

    cliente10 = Cliente("Camila", "camila@gmail.com")
    servicio10 = ReservaSala(1)

    reserva10 = Reserva(cliente10, servicio10)
    reserva10.confirmar()

    print(reserva10.mostrar_reserva())

except Exception as e:

    print("Error:", e)
    guardar_log(e)
