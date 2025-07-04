print("--------------------------------------")
print("         RATEIO DE DESPESA            ")
print("--------------------------------------\n\n")

print("CONSUMO PRINCIPAL         \n")

print("CONSUMO:")
cons_1 = input("Digite o item consumido: ")
qtd = int(input("Quantidade consumida: "))
preco = float(input("Preço unitario R$:"))
print(" \n ")

print("COUVERT ARTISTICO")

couv = float(input("Digite o valor do couvert R$: "))
print(" \n ")
print("GORJETAS")

gorj = float(input("Digite o valor da gorjeta recebida R$: "))
print(" \n ")

print("TAXAS DE SERVIÇOB")

print("Taxa de serviço = 10%\n")


gp = int(input("Digite o quantidade de pessoas:"))


cons = qtd*preco
tx = couv + gorj
txserv = 0.1 * cons
subtotal = cons + txserv + tx
total = subtotal / gp
print("O valor total de consumo é R$: ",cons)
print("O valor total das taxas é R$: ",tx)
print("O valor da taxa de serviço è R$: ",txserv)
print("O subtotal é R$:",subtotal)
print("O valor total a pagar de cada pessoa é R$: ",total)
