# CARLOS VITOR SOARES SANTOS, DERYSON JUNIO SILVA DE OLIVEIRA, MIGUEL BATISTA MONTEIRO

usuarios = ["admin"]
senhas = ["admin"]
titulo = []
preco = []
descricao = []


while True:
    print("1 - Adicionar usuário no sistema")
    print("2 - Entrar no sistema")
    print("3 - Sair")
    decisao = int(input("Digite a opção desejada: "))

    if decisao == 1:
        novo_usuario = input("Digite o nome do novo usuário: ")
        nova_senha = input("Digite a senha do novo usuário: ")
        usuarios.append(novo_usuario)
        senhas.append(nova_senha)
        print("Usuário cadastrado com sucesso!")

    elif decisao == 2:

        tentativa = 0

        while True:
            usuario = input("Digite o usuário: ")
            senha = input("Digite a senha: ")

            achou = False
            for i in range(len(usuarios)):
                if usuarios[i] == usuario and senhas[i] == senha:
                    achou = True

            if achou == True:
                print("Login bem-sucedido!")

                while True:
                    print("1 - Mostrar alimentos cadastrados")
                    print("2 - Cadastrar novos alimentos")
                    print("3 - Sair")
                    decisao2 = int(input("Digite a opção desejada: "))

                    if decisao2 == 1:
                        if len(titulo) == 0:
                            print("Nenhum alimento cadastrado.")
                        for i in range(len(titulo)):
                            print(titulo[i], "- R$", preco[i], "-", descricao[i])

                    elif decisao2 == 2:
                        titulo.append(input("Digite o titulo do produto: "))
                        preco.append(input("Digite o preço do produto: "))
                        descricao.append(input("Digite a descrição do produto: "))
                        print("Produto cadastrado!")

                    elif decisao2 == 3:
                        break

                    else:
                        print("Digite um número válido")

                break

            else:
                tentativa += 1
                print("Usuário ou senha incorretos. Tentativa:", tentativa)
                if tentativa >= 4:
                    print("Usuário bloqueado")
                    break
                elif tentativa >= 3:
                    print("Atenção! Você tem apenas 1 tentativa restante.")

    elif decisao == 3:
        break

    else:
        print("Digite um número válido")