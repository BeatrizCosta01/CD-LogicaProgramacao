print('\n' + '='*30)
print('      -- BEM-VINDO AO PRIME --      ')
print('='*30)

nome = input("Digite o seu nome: ")
renda = float(input("Sua renda mensal (R$): "))
gasto_mensal = float(input("Seu gasto mensal médio (R$): "))

print('\n' + '-'*10 + ' DIAGNÓSTICO ' + '-'*10)
sobra = renda - gasto_mensal
reserva_objetivo = gasto_mensal * 6

if sobra <= 0:
    print(f"⚠️ EMERGÊNCIA FINANCEIRA, {nome}!")
    print(f"Seus gastos (R${gasto_mensal:.2f}) superam ou igualam sua renda.")
    print("Dica: Antes de investir, precisamos equilibrar suas contas.")
else:
    print(f"Sua renda R${renda:.2f} supera seus gastos em R${sobra:.2f}")
    
    print('\n' + '-'*10 + ' PLANO DE AÇÃO ' + '-'*10)
    print("1- Começar a Investir")
    print("2- Formar Reserva")
    print("0- Não pretendo realocar o excedente")
    opcao = int(input('Qual o seu próximo passo? '))

    if opcao == 1:
        print('\n' + '-'*10 + ' PERFIL DE INVESTIMENTO ' + '-'*10)
        coragem = int(input("Seu nível de coragem (1 a 10): "))
        
        if coragem < 4:
            perfil = "MEDROSO (Conservador)"
            recomendacao = "Tesouro Direto"
        elif 4 <= coragem <= 7:
            perfil = "CAUTELOSO (Moderado)"
            recomendacao = "Fundos Imobiliários"
        else:
            perfil = "CORAJOSO (Arrojado)"
            recomendacao = "Ações de Tecnologia"
        
        print(f"Seu DNA Financeiro: {perfil}")
        print(f"Sugestão do PRIME: {recomendacao}")

        opcao2 = int(input(f'\n{nome}, deseja ver quanto renderia no {recomendacao}? (1- Sim / 2- Não): '))
        if opcao2 == 1:
            print('\n' + '-'*10 + ' MÁQUINA DO TEMPO ' + '-'*10)
            anos = int(input("Quantos anos você pretende investir? "))
            taxa_estimada = 0.08 
            valor_acumulado = 0

            for ano in range(1, anos + 1):
                valor_acumulado = valor_acumulado + (sobra*(1 + taxa_estimada))
                print(f"Ano {ano}: R$ {valor_acumulado:.2f}")

            print(f"\nResultado Final: Em {anos} anos, você poderá ter aproximadamente R${valor_acumulado:.2f}!")
        else:
            print("Tudo bem. Encerrando o simulador.")

    elif opcao == 2:
        print(f"\nOlá {nome}! Você tem R${sobra:.2f} livres por mês.")
        print(f"Sua meta de Reserva de Segurança (6 meses de gastos) é: R${reserva_objetivo:.2f}")
        meses = reserva_objetivo / sobra
        print(f"No seu ritmo atual, você levará {meses:.1f} meses para formá-la.")

    elif opcao == 0:
        print(f'\n{nome}, obrigado por utilizar o PRIME!! Volte sempre!!!')
    
    else:
        print('Opção inválida. Reinicie o programa.')