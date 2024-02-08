import json

# Carregando os dados do faturamento mensal de um arquivo JSON
with open('faturamento.json', 'r') as file:
    faturamento_mensal = json.load(file)

def calcular_estatisticas(faturamento):
    menor_valor = min(faturamento)
    maior_valor = max(faturamento)
    media_mensal = sum(faturamento) / len(faturamento)
    dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)
    return menor_valor, maior_valor, dias_acima_da_media

menor, maior, acima_media = calcular_estatisticas(faturamento_mensal)
print("Menor valor de faturamento diário:", menor)
print("Maior valor de faturamento diário:", maior)
print("Número de dias com faturamento acima da média mensal:", acima_media)
