def computador_escolhe_jogada(n, m):
    i = 1
    while i != m:
        if ((n - i) % (m + 1)) == 0:
            return i
        i = i + 1
    return m
def usuario_escolhe_jogada(n, m):
    jogUs = -1
    while jogUs < 1 or jogUs > m or jogUs > n:
        jogUs = int(input("\nQuantas peças você vai tirar? "))
        if jogUs < 1 or jogUs > m or jogUs > n:
            print("\nOops! Jogada inválida! Tente de novo.")
    return jogUs
def partida():
    n = int(input("\nQuantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    i = 0
    if n % (m + 1) == 0:
        print("\nVoce começa!")
        jogUs = usuario_escolhe_jogada(n, m)
        if jogUs == 1:
            print("\nVocê tirou uma peça.")
            n = n - jogUs
            if n != 0:
                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                else:
                    print("Agora restam", n, "peças no tabuleiro.")
        else:
            print("Você tirou" ,jogUs, "peças.")
            n = n - jogUs
            if n != 0:
                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                else:
                    print("Agora restam", n, "peças no tabuleiro.")
    else:
        print("\nComputador começa!")
        i = i + 1
        jogComp = computador_escolhe_jogada(n, m)
        if jogComp == 1:
            print("\nO computador tirou uma peça.")
            n = n - jogComp
            if n != 0:
                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                else:
                    print("Agora restam", n, "peças no tabuleiro.")
        else:
            print("\nO computador tirou" ,jogComp, "peças.")
            n = n - jogComp
            if n != 0:
                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                else:
                    print("Agora restam", n, "peças no tabuleiro.")
    while n != 0:
        if i % 2 != 0:
            i = i + 1
            jogUs = usuario_escolhe_jogada(n, m)
            if jogUs == 1:
                print("\nVocê tirou uma peça.")
                n = n - jogUs
                if n != 0:
                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.")
                    else:
                        print("Agora restam", n, "peças no tabuleiro.")
            else:
                print("Você tirou" ,jogUs, "peças.")
                n = n - jogUs
                if n != 0:
                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.")
                    else:
                        print("Agora restam", n, "peças no tabuleiro.")
        else:
            i = i + 1 
            jogComp = computador_escolhe_jogada(n, m)
            if jogComp == 1:
                print("\nO computador tirou uma peça.")
                n = n - jogComp
                if n != 0:
                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.")
                    else:
                        print("Agora restam", n, "peças no tabuleiro.")
            else:
                print("\nO computador tirou", jogComp, "peças.")
                n = n - jogComp
                if n != 0:
                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.")
                    else:
                        print("Agora restam", n, "peças no tabuleiro.")
    if i % 2 != 0:
        print("Fim do jogo! O computador ganhou!\n")
        return i
    else:
        print("Fim do jogo! Você ganhou!\n")
        return i
def campeonato():
    i = 0
    result =0
    scoreUs = 0
    scoreComp = 0
    print()
    while i != 3:
        print("**** Rodada", i+1, "****")
        result = partida()
        if result % 2 != 0:
            scoreComp = scoreComp + 1
        else:
            scoreUs = scoreUs + 1
        i = i + 1
    print("**** Final do campeonato! ****")
    print("\nPlacar: Você", scoreUs, "X", scoreComp, "Computador")

print("Bem-vindo ao jogo do NIM! Escolha:")
print("\n1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
escolha = int(input())

if(escolha == 1):
    print("\nVoce escolheu uma partida!")
    partida()
else:
    print("Voce escolheu um campeonato!\n")
    campeonato()