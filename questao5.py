def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

texto = input("Digite uma string: ")
print(f"String invertida: {inverter_string(texto)}")
