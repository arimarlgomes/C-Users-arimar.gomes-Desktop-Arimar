#CRIAR PROJETO
#1 - iDENTIFICAR UM PROBLEMA, PODENDO SER FICTÍCIO;
#2 - SOLUÇÃO DO PROBLEMA EM PYTHON;
#3 - O PROJETO DEVE ESTÁ CLEAN E LAYOUT AGRADÁVEL;
#4 - PROJETO DEVE ESTÁ COMPLETO;
#5 - DEVE SER APRESENTADO.


print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

print("_______Registro de produto________")

print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

print("Cadastro de produto")
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

print("Produto 1")
print("Cadastrar produto:")
id_1 = input("Digite o código de identificação do produto: ")
prod_1 = input("Digite o nome do produto: ")
qtd_1 = int(input("Quantidade do produto: "))
val_1 = (input("Digite a data de validade do produto: "))
preco_1 = float(input("Preço unitario Produto:R$ "))

print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

print("Produto 2")
print("Cadastrar produto:")
id_2 = input("Digite o código de identificação do produto: ")
prod_2 = input("Digite o nome do produto: ")
qtd_2 = int(input("Quantidade do produto: "))
val_2 = input("Digite a data de validade do produto: ")
preco_2 = float(input("Preço unitario Produto:R$ "))

print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

print("Produto 3")
print("Cadastrar produto:")
id_3 = input("Digite o código de identificação do produto: ")
prod_3 = input("Digite o nome do produto: ")
qtd_3 = int(input("Quantidade do produto: "))
val_3 = input("Digite a data de validade do produto: ")
preco_3 =float(input("Preço unitario Produto:R$ "))

print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

print("Produto 4")
print("Cadastrar produto:")
id_4 = input("Digite o código de identificação do produto: ")
prod_4 = input("Digite o nome do produto: ")
qtd_4 = int(input("Quantidade do produto: "))
val_4 = input("Digite a data de validade do produto: ")
preco_4 = float(input("Preço unitario Produto:R$ "))

print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

print("Produto 5")
print("Cadastrar produto:")
id_5 = input("Digite o código de identificação do produto: ")
prod_5 = input("Digite o nome do produto: ")
qtd_5 = int(input("Quantidade do produto: "))
val_5 = input("Digite a data de validade do produto: ")
preco_5 = float(input("Preço unitario Produto:R$ "))

print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

print("Consultar produto:")

pesquisa = input("Digite o nome ou id do produto: ")

if pesquisa == prod_1:
    print(f"ID do produto: {id_1}")
    print(f"Nome do produto: {prod_1}")
    print(f"Quantidade do produto: {qtd_1}")
    print(f"Validade do produto: {val_1}")
    print(f"Preço do produto:R$ {preco_1}")

elif pesquisa == prod_2:
    print(f"ID do produto: {id_2}")
    print(f"Nome do produto: {prod_2}")
    print(f"Quantidade do produto: {qtd_2}")
    print(f"Validade do produto: {val_2}")
    print(f"Preço do produto:R$ {preco_2}")

elif pesquisa == prod_3:
    print(f"ID do produto: {id_3}")
    print(f"Nome do produto: {prod_3}")
    print(f"Quantidade do produto: {qtd_3}")
    print(f"Validade do produto: {val_3}")
    print(f"Preço do produto:R$ {preco_3}")

elif pesquisa == prod_4:
    print(f"ID do produto: {id_4}")
    print(f"Nome do produto: {prod_4}")
    print(f"Quantidade do produto: {qtd_4}")
    print(f"Validade do produto: {val_4}")
    print(f"Preço do produto:R$ {preco_4}")

elif pesquisa == prod_5:
    print(f"ID do produto: {id_5}")
    print(f"Nome do produto: {prod_5}")
    print(f"Quantidade do produto: {qtd_5}")
    print(f"Validade do produto: {val_5}")
    print(f"Preço do produto:R$ {preco_5}")

elif pesquisa == id_1:
    print(f"ID do produto: {id_1}")
    print(f"Nome do produto: {prod_1}")
    print(f"Quantidade do produto: {qtd_1}")
    print(f"Validade do produto: {val_1}")
    print(f"Preço do produto:R$ {preco_1}")

elif pesquisa == id_2:
    print(f"ID do produto: {id_2}")
    print(f"Nome do produto: {prod_2}")
    print(f"Quantidade do produto: {qtd_2}")
    print(f"Validade do produto: {val_2}")
    print(f"Preço do produto:R$ {preco_2}")

elif pesquisa == id_3:
    print(f"ID do produto: {id_3}")
    print(f"Nome do produto: {prod_3}")
    print(f"Quantidade do produto: {qtd_3}")
    print(f"Validade do produto: {val_3}")
    print(f"Preço do produto:R$ {preco_3}")

elif pesquisa == id_4:
    print(f"ID do produto: {id_4}")
    print(f"Nome do produto: {prod_4}")
    print(f"Quantidade do produto: {qtd_4}")
    print(f"Validade do produto: {val_4}")
    print(f"Preço do produto:R$ {preco_4}")

elif pesquisa == id_5:
    print(f"ID do produto: {id_5}")
    print(f"Nome do produto: {prod_5}")
    print(f"Quantidade do produto: {qtd_5}")
    print(f"Validade do produto: {val_5}")
    print(f"Preço do produto:R$ {preco_5}")    

else:
    print("Você não digitou uma opção válida.")

print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
pesquisa = input("Digite o nome ou id do próximo produto: ")



