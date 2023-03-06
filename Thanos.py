import random

while True:
    random.seed()
    arvore_do_thanos = random.randint(1, 50)
    
    print("\nBem vindo ao jogo do Thanos X Lanterna Verde")
    print("Thanos está escondido em uma árvore numerada de 1 a 50, tente achá-lo")
    print("Dificuldades")
    print("1-Fácil (15 tentativas)")
    print("2-Médio (10 tentativas)")
    print("3-Difícil (5 tentativas)")
    dificuldade = int(input("Escolha a dificuldade: "))
    tentativas = [15, 10, 5][dificuldade-1]
    
    for i in range(1, tentativas+1):
        print(f"Tentativa {i} de {tentativas}")
        palpite = int(input("Escolha um número: "))
        if palpite > arvore_do_thanos:
            print("Thanos está numa árvore menor.")
        elif palpite < arvore_do_thanos:
            print("Thanos está numa árvore maior.")
        else:
            print("Você achou o Thanos!")
            break
    
    if palpite != arvore_do_thanos:
        print(f"Suas tentativas acabaram. O Thanos estava na árvore {arvore_do_thanos}.")
    
    jogar_novamente = input("Deseja jogar novamente? (sim/não): ")
    if jogar_novamente.lower() != "sim":
        break
