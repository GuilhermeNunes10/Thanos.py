import random

class Tentativas():
    def __init__(self) -> None:
        self.arvore_thanos =  random.randint(1, 50)

    def iniciar(self):

        while True:
           
            self.jogo()
            
            jogar_novamente = input("\nDeseja jogar novamente? (sim/não): ")
            if jogar_novamente != "sim":
                break

    def jogo(self):
        arvore_thanos = self.arvore_thanos
            
        print("Bem vindo ao jogo do Thanos X Lanterna Verde")
        print("Thanos está escondido em uma arvore numerada de 1 a 50, tente achá-lo")
        print("Dificuldades")
        print("1-Fácil (15 tentativas)")
        print("2-Médio (10 tentativas)")
        print("3-Difícil (5 tentativas)")
        tentativas = {"1": 15, "2": 10, "3": 5}[input("Escolha a dificuldade: ")]
        
        for tentativa_atual in range(1, tentativas + 1):
            print(f"\nTentativa {tentativa_atual} de {tentativas}")
            palpite = int(input("Escolha um número: "))
            
            if palpite > arvore_thanos:
                print("Thanos está numa árvore menor")
            elif palpite < arvore_thanos:
                print("Thanos está numa árvore maior")
            else:
                print("\nVocê achou o Thanos")
                break
        else:
            print(f"\nSuas tentativas acabaram. O Thanos estava na árvore {arvore_thanos}")