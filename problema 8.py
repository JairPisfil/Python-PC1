hora_str = input("Que hora es?: ")

partes = hora_str.split(":")
horas = int(partes[0])
minutos = int(partes[1])

hora_decimal = horas + minutos / 60

if 7.0 <= hora_decimal <= 8.0:
    print("Es hora del desayuno")
elif 12.0 <= hora_decimal < 13.0:
    print("Es hora del almuerzo")
elif 18.0 <= hora_decimal < 19.0:
    print("Es hora de la cena")
