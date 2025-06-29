cantidad_payasos = int(input("Cantidad de payasos a enviar: "))
cantidad_muñecas = int(input("Cantidad de muñecas a enviar: "))
peso_payasos = 112 * cantidad_payasos
peso_muñecas = 75 * cantidad_muñecas
peso_paquete = peso_payasos + peso_muñecas
print(f"El peso total del paquete es {peso_paquete}")
