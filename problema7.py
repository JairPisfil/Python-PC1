num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("\nElige una opción:")
print("1. Mostrar la suma de los dos números")
print("2. Mostrar la resta (el primero menos el segundo)")
print("3. Mostrar la multiplicación de los dos números")

opcion = input("Opción (1, 2 o 3): ")

if opcion == "1":
    resultado = num1 + num2
    print(f"La suma es: {resultado}")
elif opcion == "2":
    resultado = num1 - num2
    print(f"La resta es: {resultado}")
elif opcion == "3":
    resultado = num1 * num2
    print(f"La multiplicacion es: {resultado}")
else:
    print("Opcion invalida.")