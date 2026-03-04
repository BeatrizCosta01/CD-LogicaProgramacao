def LimparVendas(vendasFilial):
    vendas_limpas = []

    for valor in vendasFilial:
        if valor > 0:
            if valor < 10000:
                vendas_limpas.append(valor)
                
    return vendas_limpas

def AnalizarDados(a):
    faturamentoTotal = sum(a)
    mediaVendas = faturamentoTotal/len(vendasLimpas)
    return faturamentoTotal, mediaVendas

def definirStatus(media):
    if 2000 <= media <= 5000:
        return 'Performance Estável'
    elif media > 5000:
        return 'Alta Performance'
    else:
        return 'Performance Crítica'

print(f'\n-- Pipeline de Auditoria para Ciência de Dados --\n')

vendasFilial = []

nome = input('Informe o nome da Filial: ')

valor = float(input('Insira o Valor da Venda (ou 0 para parar): '))
while valor != 0:
    if valor == 0:
        vendasFilial.pop() 
        break
    else:
        vendasFilial.append(valor)
        valor = float(input('Insira o Valor da Venda (ou 0 para parar): '))

vendasLimpas = LimparVendas(vendasFilial)
analizeDados = AnalizarDados(vendasLimpas)

print(f'-' *30)
print(f'\n -- Relatório Filial {nome}')
print(f'Performance: {definirStatus(analizeDados[1])}')
print(f'Faturamento Total: {analizeDados[0]:.2f}')
print(f'Média de Vendas: {analizeDados[1]:.2f}')

print(f'\n-- LISTA DE VENDAS --')

for i, venda in enumerate(vendasLimpas):
    print(f'{i + 1} Venda: {venda}')