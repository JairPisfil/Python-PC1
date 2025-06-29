costo_comida = float(input("Cuanto costo la comida?: "))
porcentaje_propina = float(input("Que porcentje de propina desea dejar al mesero?: "))
Propina = (porcentaje_propina/100) * costo_comida
print(f"Propina ${Propina: .2f}")
