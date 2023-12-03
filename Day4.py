import random

jokempo = ["pedra", "papel", "tesoura"]
escolha = int(input("Escolha:\n1-Pedra\n2-Papel\n3-Tesoura\n4-Finalizar\n"))
while escolha > 4:
        escolha = int(input("Escolha:\n1-Pedra\n2-Papel\n3-Tesoura\n4-Finalizar\n"))
while(escolha != 4):
    pc = random.randint(0, 2)
    print(f"Escolha do PC: {jokempo[pc]}")
    print(f"Sua escolha: {jokempo[escolha-1]}")
    if jokempo[pc] == "tesoura" and escolha == 3:
        print("Empatou!")
    elif jokempo[pc] == "tesoura" and escolha == 2:
        print("PC Ganhou!")
    elif jokempo[pc] == "tesoura" and escolha == 1:
        print("Você Ganhou!")
    elif jokempo[pc] == "papel" and escolha == 3:
        print("Você Ganhou!")
    elif jokempo[pc] == "papel" and escolha == 2:
        print("Empatou!")
    elif jokempo[pc] == "papel" and escolha == 1:
        print("PC Ganhou!")
    elif jokempo[pc] == "pedra" and escolha == 3:
        print("PC Ganhou!")
    elif jokempo[pc] == "pedra" and escolha == 2:
        print("Você Ganhou!")
    elif jokempo[pc] == "pedra" and escolha == 1:
        print("Empatou!")
    escolha = int(input("Escolha\n1-Pedra\n2-Papel\n3-Tesoura\n4-Finalizar\n"))
    while escolha > 4:
        escolha = int(input("Escolha:\n1-Pedra\n2-Papel\n3-Tesoura\n4-Finalizar\n"))
