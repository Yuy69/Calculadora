while True:  # Loop principal (menu)

    print("""
===========CalculadoraV1=========

---------------------
[1] Adição
---------------------
[2] Subtração
---------------------
[3] Multiplicação
---------------------
[4] Divisão
---------------------
[5] Fechar
---------------------
""")

    opcoes = input("Qual operação você deseja? R°=")

    # <3================= ADIÇÃO =================<3
    if opcoes == "1":

        while True:     #Este whilhe cria um loop na estrutura de repetição em específico na parte do cálculo.
            try:        #Este try tenta executar o cálculo ma se caso o usuário não digitar um "float" nos input numero 1 e numero2 então ele cai na exceção "except".
                        #Aqui começa a parte responsável pelo calculo onde o usuário digite os números que ele deseja calcular.
                numero1 = float(input("Digite um número:\nR°="))
                numero2 = float(input("Digite outro número:\nR°="))
                calculo = numero1 + numero2 
                print(f"Resultado: {calculo:.2f}")
                break  #Nesta parte se o usuário digitar tipos "float válidos" acaba o calculo e chega em fim no break que quebra o laço (while) loop da estrutura de repetição.

            except:    #Este é except (exceção) do try (tente) realizar o cálculo de adição mas caso o usuário tente digitar caracteres ao invés de números então cai na exceção que resolve o valueerror.
                print("Por favor digite apenas números") #Está mensagem só aparecera se o except for acionada ou seja o usuário escolha caracteres dentro da estrutura de adição.
                       #uma obs importante é que caso caia no except o break não é acionado então o loop do primeiro while não é quebrado mantendo o usuário preso no "digite um númro" até escolher um tipo "float" válido.

        while True:    #Este while abre um laço no menu "pós cálculo" até ele escolher algo válido
            print("[1] Voltar ao menu")
            print("[2] Continuar somando")
            print("[3] Encerrar o programa")

            continuar = input("O que deseja?\nR°=")

            if continuar == "1":   #Caso o usuário escolher a opção número "1" ele acionara o break que encerra o while e volta para o loop inicial que seria o menu principal.
                break

            elif continuar == "2":  #Aqui cai para o usuário fazer um cálculo com o número resultante de sua operação anterior.
                while True:         #Laço aberto para "forçar" o usuário digitar opções válidas.
                    try:            #Aqui o "try" tenta realizar o cálculo se as opções do usuário forem "float" válidos.
                        numero = float(input("Digite um número: "))
                        calculo += numero
                        print(f"Novo resultado: {calculo:.2f}")
                        break
                    except:     #Se o usuário colocar caracteres cai neste except que o adverte de sua escolha.
                        print("Por favor digite apenas números")

            elif continuar == "3":   #aqui basicamente o usuário escolhe fechar o programa e o "exit()" faz isso fecha tudo encerrando o programa de vez
                print("Encerrando...")
                exit()

            else:             #se o usuário não escolher nenhuma das opções do menu "pós" cálculo então o else aciona uma mensagem que o adverte.
                print("Opção inválida!")  

    # <3================= SUBTRAÇÃO =================<3
    elif opcoes == "2":

        while True:
            try:
                numero1 = float(input("Digite um número:\nR°="))
                numero2 = float(input("Digite outro número:\nR°="))
                calculo = numero1 - numero2
                print(f"Resultado: {calculo:.2f}")
                break
            except:
                print("Por favor digite apenas números")

        while True:
            print("[1] Voltar ao menu")
            print("[2] Continuar subtraindo")
            print("[3] Encerrar o programa")

            continuar = input("O que deseja?\nR°=")

            if continuar == "1":
                break

            elif continuar == "2":
                while True:
                    try:
                        numero = float(input("Digite um número: "))
                        calculo -= numero
                        print(f"Novo resultado: {calculo:.2f}")
                        break
                    except:
                        print("Por favor digite apenas números")

            elif continuar == "3":
                print("Encerrando...")
                exit()

            else:
                print("Opção inválida!")

    # <3================= MULTIPLICAÇÃO =================<3
    elif opcoes == "3":

        while True:
            try:
                numero1 = float(input("Digite um número:\nR°="))
                numero2 = float(input("Digite outro número:\nR°="))
                calculo = numero1 * numero2
                print(f"Resultado: {calculo:.2f}")
                break
            except:
                print("Por favor digite apenas números")

        while True:
            print("[1] Voltar ao menu")
            print("[2] Continuar multiplicando")
            print("[3] Encerrar o programa")

            continuar = input("O que deseja?\nR°=")

            if continuar == "1":
                break

            elif continuar == "2":
                while True:
                    try:
                        numero = float(input("Digite um número: "))
                        calculo *= numero
                        print(f"Novo resultado: {calculo:.2f}")
                        break
                    except:
                        print("Por favor digite apenas números")

            elif continuar == "3":
                print("Encerrando...")
                exit()

            else:
                print("Opção inválida!")

    # <3================= DIVISÃO =================<3
    elif opcoes == "4":

        while True:
            try:
                numero1 = float(input("Digite um número:\nR°="))
                numero2 = float(input("Digite outro número:\nR°="))

                if numero2 == 0:
                    print("Erro: não existe divisão por zero!")
                    continue

                calculo = numero1 / numero2
                print(f"Resultado: {calculo:.2f}")
                break
            except:
                print("Por favor digite apenas números")

        while True:
            print("[1] Voltar ao menu")
            print("[2] Continuar dividindo")
            print("[3] Encerrar o programa")

            continuar = input("O que deseja?\nR°=")

            if continuar == "1":
                break

            elif continuar == "2":
                while True:
                    try:
                        numero = float(input("Digite um número: "))

                        if numero == 0:
                            print("Erro: não pode dividir por zero!")
                        else:
                            calculo /= numero
                            print(f"Novo resultado: {calculo:.2f}")
                            break
                    except:
                        print("Por favor digite apenas números")

            elif continuar == "3":
                print("Encerrando...")
                exit()

            else:
                print("Opção inválida!")

    # <3================= SAIR =================<3
    elif opcoes == "5":
        print("Encerrando...")
        break

    # <3================= ERRO =================<3
    else:      
        print(f"Opção ({opcoes}) inválida! Escolha entre [1-5].")