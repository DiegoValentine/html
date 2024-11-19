import random

def jogo_adivinhacao():
    print("Bem-vindo ao jogo de adivinhação!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    print("Estou pensando em um número entre 1 e 100. Tente adivinhá-lo!")

    while not acertou:
        try:
            tentativa = int(input("Adivinhe um número: "))
            if tentativa < 1 or tentativa > 100:
                print("Por favor, escolha um número entre 1 e 100.")
                continue
            
            tentativas += 1
            
            if tentativa < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif tentativa > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                acertou = True
                print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")

        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")

if __name__ == "__main__":
    jogo_adivinhacao()
