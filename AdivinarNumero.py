import random

hidden = random.randint(1, 100)
guess = int

nombre = str(input("Hola! Ingresa tu nombre para continuar: "))
print("Bienvenido " + nombre)

while hidden != guess:
    guess = int(input("Ingresá un número entre 1 y 100: "))
    if guess > hidden:
        print('El número es demasiado grande!')
    if guess < hidden:
        print('El número es demasiado pequeño!')
    if guess == hidden:
        break

print("Adivinaste!")

input("Apreta cualquier tecla para cerrar")