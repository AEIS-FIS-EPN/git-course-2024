print("Bienvenido al programa")

response1 = int(input("Ingresa un número: "))
response2 = int(input("Ingresa otro número: "))


def sum(num1, num2):
    return num1 + num2


print(f"El resultado de tu suma es: {sum(response1, response2)}")
