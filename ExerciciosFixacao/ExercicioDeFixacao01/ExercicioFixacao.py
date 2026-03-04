# EXERCÍCIOS DE FIXAÇÃO E APRENDIZADO - L1
# Tayllor Beatriz Queiroz Costa
#     1.OPERADORES

# 1.1 Aritméticos
# print('-- ⭐Aritméticos⭐--')

# n1= int(input('Digite o Primeiro número para os Calculos:'))
# n2= int(input('Digite o Segundo número para os Calculos:'))

# print('-'*30)
# print('-- RESULTADOS --')
# print(f'SOMA: {n1 + n2}')
# print(f'SUBTRAÇÃO: {n1 - n2}')
# print(f'MULTIPLICAÇÃO: {n1 * n2}')
# print(f'DIVISÃO REAL: {n1 / n2}')
# print(f'DIVISÃO INTEIRA: {n1 // n2}')
# print(f'RESTO DA DIVISÃO: {n1 % n2}')

# 1.2 Atribuição
# print('-- ⭐Atribuição⭐--')
# saldo = 1000
# saldo += 500
# saldo -= 200
# saldo *= 2

# print(f'O saldo final foi de R${saldo:.2f}')

# 1.3 Comparação
# print('-- ⭐Comparação⭐--')

# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))

# maior = num1 > num2
# iguais = num1 == num2
# diferente = num1 != num2

# print(f"\nResultados para {num1} e {num2}:")
# print(f"O primeiro é maior que o segundo? {maior}")
# print(f"Eles são iguais? {iguais}")
# print(f"O primeiro é diferente do segundo? {diferente}")

# 1.4 Lógicos
# print('-- ⭐Lógicos⭐--')
# presensa = int(input('Digite o quantidade de presença do aluno: '))
# media = float(input('Digite a média do aluno: '))
# #print(f'vc esta {apto* aprovado}{rep*reprovado}')
# print('O Aluno Foi Aprovado' if presensa >= 75 and media >= 7 else 'O aluno foi Reprovado')

# 1.5  Identidade
# print('-- ⭐Identidade⭐--')
# a = [1, 2]
# b = [1, 2]
# c = a
# print(f"a is b? {a is b}")    
# print(f"a is c? {a is c}")  


# 1.6  Associação 

# print('-- ⭐Associação ⭐--')
# frase = "Ciência de Dados"

# tem_D = "D" in frase

# nao_tem_python = "Python" not in frase

# print(f"O caractere 'D' está na frase? {tem_D}")
# print(f"A palavra 'Python' não está na frase? {nao_tem_python}")

#     2.Estrutura Condicional

# print('-- ⭐Classificação Natação ⭐--')
# idade = int(input('Digite a idade: '))

# if (idade >= 5) and (idade <= 12):
#     print('Categoria de Nadador: INFANTIL')
# elif (idade >= 13) and (idade <= 17):
#     print('Categoria de Nadador: JUVENIL')
# elif idade >= 18 :
#     print('Categoria de Nadador: ADULTO')
# else:
#     print('Não existe essa categoria de idade para natação')

#     3.Estrutura de Repetição FOR

# numero = int(input("Digite um número inteiro para ver a tabuada: "))

# print(f"\nTabuada de {numero}:")
# print("-" * 15)

# for i in range(1, 11):
#     resultado = numero * i
#     print(f"{numero} x {i:2} = {resultado}")

# print("-" * 15)

#     4.Estrutura de Repetição WHILE
# print('-- ⭐DIGITE A SENHA ⭐--')
# while True:
#     senha = input('Digite a senha: ')
#     if senha == "python123":
#         print('Acesso Permitido!!')
#         break
#     else:
#         print('Senha Incorreta')




