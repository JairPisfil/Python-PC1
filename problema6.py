edad_cliente = int(input("Cual es su edad?: "))

if edad_cliente < 4:
    precio = 0
if 4 < edad_cliente < 18:
    precio = 5
if edad_cliente > 18:
    precio = 10

print(f"El precio de la entrada es: ${precio}")
