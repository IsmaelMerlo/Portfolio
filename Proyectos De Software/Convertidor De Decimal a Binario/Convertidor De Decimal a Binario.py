def binario(decimal):
    binario = ""
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

number = int(input("Introduce el número que quieres convertir a binario: "))
print(binario(number))