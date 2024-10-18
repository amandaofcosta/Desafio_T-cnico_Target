def pertence_fibonacci(numero):
    a, b = 0, 1
    while a <= numero:
        if a == numero:
            return f"O número {numero} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"O número {numero} NÃO pertence à sequência de Fibonacci."

numero = int(input("Digite um número: "))
print(pertence_fibonacci(numero))
