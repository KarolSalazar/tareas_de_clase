def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mueve el disco 1 de {origen} a {destino}")
    else:
        hanoi(n-1, origen, auxiliar, destino)
        print(f"Mueve el disco {n} de {origen} a {destino}")
        hanoi(n-1, auxiliar, destino, origen)

# Menú de usuario
print("Torre de Hanoi")
while True:
    try:
        discos = int(input("Discos a usar:"))
        if discos <= 0:
            print("No puedes jugar con 0 dicos")
        else:
            break
    except ValueError:
        print("No puede jugar con discos medios")

print(f"Hay {discos} discos")
print("Pasos a seguir:")
hanoi(discos, "A", "C", "B")