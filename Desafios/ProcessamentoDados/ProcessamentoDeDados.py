# Dados iniciais
vendas_brutas = [(101, "Monitor", 5, 1200.0), (102, "Mouse", 50, 80.0), (103, "Teclado", 8, 150.0), (104, "Case", 3, 50.0)]

estoque_baixo = []
vendas_atualizadas = []
valor_total_estoque = 0

for produto in vendas_brutas:
    id_prod = produto[0]
    nome    = produto[1]
    qtd     = produto[2]
    preco   = produto[3]

    if qtd < 10:
        estoque_baixo.append(produto)

    valor_total_estoque = valor_total_estoque + (qtd * preco)

    novo_preco = preco * 1.10
    nova_tupla = (id_prod, nome, qtd, novo_preco)
    vendas_atualizadas.append(nova_tupla)


print("Produtos acabando:", estoque_baixo)
print("Valor total na loja: R$", valor_total_estoque)
print("Tabela com preços novos:", vendas_atualizadas)