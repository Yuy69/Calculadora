while True:                     #Aqui a ideia pricipal é ter um while principal que faça tudo se manter em loop infinito e principalmente retornar ao menu sempre que necessario.

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

        numero1 = float(input("Digite um número: "))
        numero2 = float(input("Digite outro número: "))
        calculo = numero1 + numero2

        print(f"Resultado: {calculo:.2f}")

        while True:                                #Novos whiles True criados para abrir novas repetições como "gavetas" abertas dentro de outras "gavetas"
            continuar = input("""
[1] Voltar ao menu
[2] Continuar somando
[3] Encerrar
R°=
""")

            if continuar == "1":
                break                       #Este break tem a função de quebrar a "gaveta" que guarda as opções da cadeia de adição e voltar para o while pricipal ou seja menu

            elif continuar == "2":
                numero = float(input("Digite um número: "))
                calculo += numero  
                print(f"Novo resultado: {calculo:.2f}")

            elif continuar == "3":
                print("Encerrando...")
                exit()        #Este aprendi por agora ele basicamente encerra tudo de vez, muito util neste caso e basicamente quando a "gaveta" onde ele esta é aberta tudo é encerrado imediatamente.

            else:
                print("Opção inválida!")

    # <3================= SUBTRAÇÃO =================<3

    elif opcoes == "2":

        numero1 = float(input("Digite um número: "))
        numero2 = float(input("Digite outro número: "))
        calculo = numero1 - numero2

        print(f"Resultado: {calculo:.2f}")

        while True:                       #Novos whiles True criados para abrir novas repetições como "gavetas" abertas dentro de outras "gavetas"
            continuar = input("""
[1] Voltar ao menu
[2] Continuar subtraindo
[3] Encerrar
R°=
""")

            if continuar == "1":
                break                         #Este break tem a função de quebrar a "gaveta" que guarda as opções da cadeia de adição e voltar para o while pricipal ou seja menu

            elif continuar == "2":
                numero = float(input("Digite um número: "))
                calculo -= numero
                print(f"Novo resultado: {calculo:.2f}")

            elif continuar == "3":
                print("Encerrando...")
                exit()       #Este aprendi por agora ele basicamente encerra tudo de vez muito util neste caso e basicamente quando a "gaveta" onde ele esta é aberta tudo é encerrado imediatamente.

            else:
                print("Opção inválida!")


    # <3================= MULTIPLICAÇÃO =================<3

    elif opcoes == "3":

        numero1 = float(input("Digite um número: "))
        numero2 = float(input("Digite outro número: "))
        calculo = numero1 * numero2

        print(f"Resultado: {calculo:.2f}")

        while True:                             #Novos whiles True criados para abrir novas repetições como "gavetas" abertas dentro de outras "gavetas"
            continuar = input("""
[1] Voltar ao menu
[2] Continuar multiplicando
[3] Encerrar
R°=
""")

            if continuar == "1":
                break                        #Este break tem a função de quebrar a "gaveta" que guarda as opções da cadeia de adição e voltar para o while pricipal ou seja menu

            elif continuar == "2":
                numero = float(input("Digite um número: "))
                calculo *= numero
                print(f"Novo resultado: {calculo:.2f}")

            elif continuar == "3":
                print("Encerrando...")
                exit()                   #Este aprendi por agora ele basicamente encerra tudo de vez muito util neste caso e basicamente quando a "gaveta" onde ele esta é aberta tudo é encerrado imediatamente.

            else:
                print("Opção inválida!")

    # <3================= DIVISÃO =================<3

    elif opcoes == "4":

        numero1 = float(input("Digite um número: "))
        numero2 = float(input("Digite outro número: "))

        if numero2 == 0:
            print("Erro: não existe divisão por zero!")
            continue

        calculo = numero1 / numero2
        print(f"Resultado: {calculo:.2f}")

        while True:                #Novos whiles True criados para abrir novas repetições como "gavetas" abertas dentro de outras "gavetas"
            continuar = input("""
[1] Voltar ao menu
[2] Continuar dividindo
[3] Encerrar
R°=
""")

            if continuar == "1":
                break                #Este break tem a função de quebrar a "gaveta" que guarda as opções da cadeia de adição e voltar para o while pricipal ou seja menu

            elif continuar == "2":
                numero = float(input("Digite um número: "))

                if numero == 0:
                    print("Erro: não pode dividir por zero!")
                else:
                    calculo /= numero
                    print(f"Novo resultado: {calculo:.2f}")

            elif continuar == "3":
                print("Encerrando...")
                exit()       #Este aprendi por agora ele basicamente encerra tudo de vez muito util neste caso e basicamente quando a "gaveta" onde ele esta é aberta tudo é encerrado imediatamente.

            else:
                print("Opção inválida!")

    #<3 ================= SAIR =================<3
    elif opcoes == "5":
        print("Encerrando...")
        break                   

    #<3 ================= ERRO =================<3
    else:
        print(f"Opção ({opcoes}) inválida! Escolha entre [1-5].")  