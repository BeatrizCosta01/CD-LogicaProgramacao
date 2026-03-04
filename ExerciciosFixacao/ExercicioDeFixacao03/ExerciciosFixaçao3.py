# 1. Identidade e Atribuição
saldo_inicial = 1000.0
checkpoint = saldo_inicial
saldo_atual = saldo_inicial

print(f"Saldo Inicial: {saldo_inicial}")
print(f"Checkpoint aponta para o mesmo local de memória? {checkpoint is saldo_inicial}")

# 2. Repetição e Associação
while True:
    auditor = input("\nDigite o nome do auditor: ")
    if "*" in auditor or "#" in auditor:
        print("Erro: O nome contém caracteres proibidos (* ou #). Tente novamente.")
    else:
        break

# 3. Processamento de Lote 
for i in [1, 2, 3, 4]:
    valor_str = input("\nInsira o valor da transação: ")
    valor = float(valor_str)
    
    # 4. Condicionais e Lógica
    if valor > 500.0:
        print("Alerta: Transação de alto valor!")
    if valor < 0 and (valor * -1) > saldo_atual:
        print("Erro: Saldo insuficiente para cobrir o débito. Transação ignorada.")
    else:
        saldo_atual = saldo_atual + valor
        print("Transação processada. Saldo atual:", saldo_atual)

# 5. Resultado Final
print("\n" + "="*30)
print(f"Saldo Final: {saldo_atual}")
print(f"O saldo_final ainda é o mesmo objeto que o checkpoint? {saldo_atual is checkpoint}")
print("="*30)