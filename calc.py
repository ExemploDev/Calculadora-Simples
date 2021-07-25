print('Calculadora - Started')
print()

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

while True:
    print("""Escolha uma daz opções abaixo:\n
     1 - Somar
     2 - Subtrair
     3 - Multiplicar
     4 - Divisão
     5 - Adicionar outro número
     S - Sair do programa\n""")
    opcao = int(input('Digite a opção: '))
    print()
    if opcao == 1:
        print('O resultado da soma entre {} + {} = {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('resultado da subtração entre {} - {} = {}'.format(n1, n2, n1 - n2))
    elif opcao == 3:
        print('resultado da multiplicação entre {} x {} = {}'.format(n1, n2, n1 * n2))
    elif opcao == 4:
        print('resultado da divisão entre {} ÷ {} = {}'.format(n1, n2, n1 / n2))
    elif opcao == 5:
        n2 = int(input('Digite um numero inteiro: '))
    elif opcao == s or opcao == S:
        break
    else:
         print('ERRO!!! Operacao Invalida')

# segue no twitter lá, ta na bio :)
# Uma Simples Calculadora, para usarem, logo trarei uma mais avançada e tals, com gui
