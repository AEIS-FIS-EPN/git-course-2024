print("Bienvenido al programa")

response1 = int(input("Ingresa un número: "))
response2 = int(input("Ingresa otro número: "))


# Está función sirve para sumar dos números
def sum(num1, num2):
    return num1 + num2


# Está función sirve para restar dos números
def substract(num1, num2):
    return num1 - num2


print(f"El resultado de la suma es: {sum(response1, response2)}")
print(f"El resultado de la resta es: {substract(response1, response2)}")
