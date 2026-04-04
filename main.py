while True:


    print("""
    ===========CalculadoraV1=========

    ---------------------
    [1]Adição
    ---------------------
    [2]Subtração
    ---------------------
    [3]Multiplição
    ---------------------
    [4]Divisão
    ---------------------
    [5]Fechar
    ---------------------

    ==================================
    """)



    opcoes = input("Qual operação você deseja?")

    if opcoes == "1":
        numero1 = float(input("Digite um número.."))         #Este bloco representa o parte responsável por fazer o cálculo de adição.
        numero2 = float(input("digite outro número.."))
        calculo = numero1 + numero2
        print(f"O resultado de sua operação foi:{calculo:.2f}")
        continuar = input("Deseja voltar o menu se sim digite:[S] se não digite:[N]..").upper()
        if continuar == "S":
            print()
            

        elif continuar == "N":
            print("Encerrando..")
            break
        



    elif opcoes == "2":
        numero1 = float(input("Digite um número.."))          #Este bloco representa a parte responsável por fazer o cálculo de subtração.
        numero2 = float(input("Digite outro número.."))
        calculo = numero1 - numero2
        print(f"O resultado de sua operação foi: {calculo:.2f}")
        continuar = input("Deseja voltar o menu se sim digite:[S] se não digite:[N]..").upper()
        if continuar == "S":
            print()
            

        elif continuar == "N":
            print("Encerrando..")
            break
        


    elif opcoes == "3":
        numero1 = float(input("Digite um número.."))            #Este bloco representa a parte responsável por fazer o cálculo de multiplicação.
        numero2 = float(input("Digite outro número.."))
        calculo = numero1 * numero2
        print(f"O resultado de sua operação foi: {calculo:.2f}")
        continuar = input("Deseja voltar o menu se sim digite:[S] se não digite:[N]..").upper()
        if continuar == "S":
            print()
            

        elif continuar == "N":
            print("Encerrando..")
            break
        
    elif opcoes == "4":
        numero1 = float(input("Digite um número.."))
        numero2 = float(input("Digite outro número.."))
        if numero2 == 0:      #se (número2) for igual a zero da erro pois zero nao pode ser dividido
          print("Desculpe, zero não pode ser dividido")  #Este bloco representa a parte responsável por fazer o cálculo de divisão.  
        
        else:
            calculo = numero1 / numero2
            print(f"O resultado de sua operação foi: {calculo:.2f}")

        continuar = input("Deseja voltar o menu se sim digite:[S] se não digite:[N]..").upper()
        if continuar == "S":
            print()
            

        elif continuar == "N":
            print("Encerrando..")
            break
        
    elif opcoes == "5":
        print("Encerrando..")
        break


    else:
        print(f"""A opção: ({opcoes}) Não existe, digite uma opção valida dentre:
    [1]
    [2]
    [3]""")    #Este else tem a função de mandar uma mensagem para o usuário de que ele não escolheu nenhuma opção que está disponível

        