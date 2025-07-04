#ATIVIDADE


print('\033[1;36;43m CALCULADORA DE JUROS SIMPLES \033[m' )
print('')
valor = float(input('VALOR INICIAL R$: '))
juros_simples = float(input('TAXA DE JUROS MENSAL %: ')) 
juros = valor * juros_simples / 100
periodo = int(input('PERIODO: '))
calc_periodo = juros * periodo
total = valor + calc_periodo
parcelas = total / periodo
print('')
print(f'\033[1;44mVALOR INICIAL R$:\033[m {valor :.2f}\n\n\033[1;45mTAXAS DE JUROS R$:\033[m {calc_periodo :.2f}\n\n\033[1;46mTOTAL FINAL R$:\033[m {total :.2f}')
print('')
print(f'\033[1;42mVALOR DAS PARCELAS R$:\033[m {parcelas :.2f}')
print('')
