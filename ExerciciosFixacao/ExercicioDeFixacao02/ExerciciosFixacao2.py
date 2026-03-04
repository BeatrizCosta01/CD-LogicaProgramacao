# 1. Integração: Operadores + Condicionais

# print(f'-- CALCULO IMC --')
# peso = float(input('Digite o seu peso: '))
# altura = float(input('Digite a sua altura em Metro: '))

# imc = (peso/(altura**2))

# if imc < 18.5 :
#     print('Você está abaixo do peso')
# elif imc >=  18.5 and imc <= 24.9:
#     print('Seu peso está normal')
# elif imc >= 25.0 and imc <= 29.9:
#     print('Você está com sobrepeso')
# else:
#     print('Você está com Obesidade')

# print(imc)

# 2. Integração: Repetição FOR + Operadores de Associação

# print(f'-- CONTAGEM DE VOGAIS --')
# frase = input("Digite uma frase ou nome completo: ")
# total_vogais = 0

# vogais = "aeiouAEIOU"

# for caractere in frase:
#     if caractere in vogais:
#         total_vogais += 1

# print(f"O total de vogais encontradas foi: {total_vogais}")

# 3. Integração: Repetição WHILE + Condicionais + Atribuição

# print('-- BANCO --')

# saldo = 500
# while True:
#     acao = int(input(f'Digite o número da ação que deseja realizar\n1 - Depositar\n2 - Sacar\n3 - Sair\n'))
#     if acao == 1 :
#         print(f'-- DEPOSITAR --\n Saldo atual: R${saldo}')
#         deposito = float(input('Digite o valor que deseja depositar: '))
#         saldo += deposito
#         print(f'Deposito realizado com sucesso\nSaldo atual: R${saldo}\n')
#     elif acao == 2:
#         print(f'-- SAQUE --\n Saldo atual: R${saldo}')
#         saque = float(input('Digite o valor que deseja sacar: '))
#         if saque > saldo:
#             print('⚠️Saldo insuficiente⚠️')
#             acao = 2
#         else:
#             saldo -= saque
#             print(f'Saque realizado com sucesso\nSaldo atual: R${saldo}\n')
#     elif acao == 3: 
#         print(f'Obrigada por utilizar o nosso Banco!!\ndesconectando da conta...')
#         break
#     else:
#         print('⚠️Nenhuma opção selecionada⚠️')

# 4. Integração: Identidade + Coleções Simples

# dados_originais = [10, 20, 30]

# dados_referencia = dados_originais

# dados_copia = [10, 20, 30]

# print(f"dados_referencia é o mesmo objeto que dados_originais? {dados_referencia is dados_originais}")

# print(f"dados_copia é o mesmo objeto que dados_originais? {dados_copia is dados_originais}")
# print(f"dados_copia tem os mesmos valores que dados_originais? {dados_copia == dados_originais}")
