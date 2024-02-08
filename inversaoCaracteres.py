def inverter_string(string):
    return ''.join(string[i] for i in range(len(string) - 1, -1, -1))

# Exemplo de uso
entrada = input("Digite uma string: ")
print("String invertida:", inverter_string(entrada))
