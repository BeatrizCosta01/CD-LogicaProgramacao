import random

conquistas = 0

def D20():
    return random.randint(1, 20)

#  Passo 1
def Inicio():
    print(f'\n--- 🌌 Bem-Vindo a Alphara-7 🌌 ---\n')
    print('Tripulante da "Exploradora Estelar": Seu objetivo é explorar a superfície do planeta Alphara-7.')
    print('Ao aterrissar, a tripulação sente a expectativa no ar. Equipados com trajes avançados, começam a exploração.')
    CondicaoExploracao()

# Passo 2
def CondicaoExploracao():
    terreno = D20()
    if terreno >= 15:
        ColetaDadosCientificos()
    elif terreno % 2 == 0:
        SuperarObstaculo()
    else:
        CondicaoExploracao()

# Passo 3
def SuperarObstaculo():
    print('\nA tripulação encontrou um obstáculo montanhoso à frente!⚠️')
    decisao = int(input('Você e a tripulação desejam:\n1 - Contornar Obstáculo\n2 - Escalar a Montanha\nEscolha: '))
    
    if decisao == 1:
        print('A equipe contornou a montanha sem problemas e continua a exploração.')
        CondicaoExploracao() 
    elif decisao == 2:
        pdObstaculo = D20()
        print(f'Tentando escalar... Dificuldade do terreno: {pdObstaculo}')
        habilidade = D20()
        print(f'Sua habilidade para superar o obstáculo: {habilidade}')

        if habilidade < pdObstaculo:
            print('A equipe não conseguiu superar o obstáculo e precisa tentar novamente.❌')
            SuperarObstaculo() 
        else:
            print('Sucesso! A montanha foi vencida.💪')
            CondicaoExploracao() 

def ColetaDadosCientificos():
    global conquistas
    print('\nA tripulação encontrou uma área rica em minerais ou sinais de vida! 💎🌲')
    
    novos_dados = D20()
    conquistas += novos_dados
    print(f'Vocês coletaram {novos_dados} novos dados. Total acumulado: {conquistas}')
    
    decisao = int(input('Desejam voltar à Nave? (1 - Sim / 2 - Não): '))
    if decisao == 1:
        print(f'\n--- FIM DA EXPEDIÇÃO ---')
        print(f'Total de conquistas científicas: {conquistas}')
        print('A tripulação retorna à Exploradora Estelar e parte de volta para a Terra com descobertas incríveis!')
    else:
        print('O espírito explorador fala mais alto! A missão continua...')
        CondicaoExploracao()
    return conquistas


Inicio()

