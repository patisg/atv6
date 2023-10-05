import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

try:

    opcao1 = 0
    opcao2 = 0

    while opcao1 not in [1, 2, 3]:
        opcao1 = float(input("\nUsuario1, escolha uma opção: \n1 - Pedra\n2- Papel\n3-Tesoura\n> "))
        if opcao1 not in [1, 2, 3] :
            print("\n\nOpção inválida. Por favor, escolha entre 1, 2 ou 3.\n\n")      

    while opcao2 not in [1, 2, 3]:
        opcao2 = float(input("\nUsuario2, escolha uma opção: \n1 - Pedra\n2- Papel\n3-Tesoura\n> "))
        if opcao2 not in [1, 2, 3] :
            print("\n\nOpção inválida. Por favor, escolha entre 1, 2 ou 3.")      

    resultado = proxy.jogo(opcao1,opcao2)
    print(proxy.resultado(resultado))
except ValueError as e:
    print("Erro: ",e)
except Exception as e:
    print("Erro: ",e)
