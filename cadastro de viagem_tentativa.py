# SITE DE VIAGEM
# CRIAR CADASTRO
# LOGIN E SENHA
# MAIOR DE 18 ANOS
# ETAPAS DE VENDAS: SAÍDA
#                   DESTINO
#                   REGIÃO
#                   TIPO DE VEÍCULO
#                   PREÇOS


print("-----------------------------------------")
print("            CADASTRO DE VIAGEM           ")
print("-----------------------------------------\n")

print ("CADASTRAR USUÁRIO\n")

user = input("Digitar Usuário: ")
log = input("Criar Senha: ")
print("\n")

print ("REGISTRAR USUÁRIO\n")
nom = input("Nome:")
idad = int(input("Idade: "))
dvia = input("Data da Viagem:")
dret = input("Data de Retorno*opcional:")
dia = int(input("Diárias"))
loc = input("Destino:")
veic = input("Tipo de Veículo:")
print("\n")

if idad >= 18:
    print(f"Usuário: {user}")
    print(f"Senha: {log}")
    print(f"Data de viagem: {dvia}")
    print(f"Data de Retorno: {dret}")
    print(f"Destino: {loc}")
    print(f"Tipo de veículo: {veic}")

else:
    print("CADASTRO INVÁLIDO")
