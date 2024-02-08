def pertence_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return "Pertence à sequência de Fibonacci" if b == numero else "Não pertence à sequência de Fibonacci"

# Exemplo de uso
numero = int(input("Digite um número: "))
print(pertence_fibonacci(numero))
