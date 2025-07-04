print("___________________________")
print("BEM VINDO AO CASSI TURISMO")
print("___________________________")

print("\n--- CADASTRO INICIAL ---")
print("Para usar o Cassi Turismo, por favor, crie seu login.")

# Captura o login e senha para a sessão
login_da_sessao = input("Crie seu nome de usuário: ")
senha_da_sessao = input("Crie sua senha: ")
idade = int(input("Digite sua idade: "))

# Variavel da idade minima e se ela é maior que 18
idade_minima = 18
permitido_entrar = False

    
if idade >= idade_minima:
        permitido_entrar = True
else:
        print(f"\nVocê precisa ter {idade_minima} anos ou mais para usar o Cassi Turismo. Acesso negado.")


# IF do programa - iniciando com a idade sendo True ☻
if permitido_entrar:
    # Loop de login
    while True:
        print("\n--- FAÇA LOGIN PARA CONTINUAR ---")
        usuario_input = input("Usuário: ")
        senha_input = input("Senha: ")

        # Verifica se o login e senha estão iguais aos input iniciais
        if usuario_input == login_da_sessao and senha_input == senha_da_sessao:
            print(f"Bem-vindo(a), {login_da_sessao}!")

            # Com o login feito, o usuario cai aqui
            while True: #Loop após o login dar certo
                print(f"\n--- OLÁ, {login_da_sessao}! ---")
                print("1. Comprar Viagem")
                print("2. Logout")
                print("3. Sair do Programa")
                escolha_logado = input("Escolha uma opção: ")

                if escolha_logado == '1':
                   
                    print("\n--- NOVA VIAGEM ---")

                    origem = input("De onde você vai partir? ")

                    destino = input("Para onde você deseja viajar? ")
                  
                    print("\nVeículos Disponíveis:")
                    print("1. Avião")
                    print("2. Ônibus")
                    print("3. Carro")
                    escolha_veiculo = input("Escolha o número do veículo: ")

                    nome_veiculo = ""
                
                    if escolha_veiculo == "1" or escolha_veiculo == "Aviao" or escolha_veiculo == "Avião":
                        nome_veiculo = "Avião"
                    elif escolha_veiculo == "2" or escolha_veiculo == "Onibus" or escolha_veiculo == "Ônibus":
                        nome_veiculo = "Ônibus"
                    elif escolha_veiculo == "3" or escolha_veiculo == "Carro" or escolha_veiculo == "carro":
                        nome_veiculo = "Carro"
                    else:
                        nome_veiculo = "Veículo Não Especificado"

                    print("\n--- RESUMO DA SUA RESERVA ---")
                    print(f"Passageiro: {login_da_sessao}")
                    print(f"Partida: {origem}")
                    print(f"Destino: {destino}")
                    print(f"Veículo: {nome_veiculo}")
                    print("Sua viagem foi reservada com sucesso!")

                elif escolha_logado == '2':
                    #Caso o faça logout o usuario vai voltar para  o loop de login
                    print(f"Fazendo logout de {login_da_sessao}...")
                    break # Para sair do Loop de Viagem
                
                elif escolha_logado == '3':
                    # --- SAIR DO PROGRAMA ---
                    print("Saindo do programa. Até mais!")
                    
                    break # Também para sair do Loop de Viagem, indo para o IF abaixo
                else:
                    print("Opção inválida. Por favor, tente novamente.")
            
            # Caso o 3 seja escolhi do acima, ela terá que sair de tudo, então segue esse IF
            if escolha_logado == '3':
                break # Sai do loop de login principal

        else:
            print("Usuário ou senha inválidos. Tente novamente.")

else:
    print("O programa será encerrado.")