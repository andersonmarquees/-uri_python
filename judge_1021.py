valor = float(input())
valor += 0.0001
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')

for nota in notas:
    num_nota = valor // nota
    valor -= nota*num_nota
    print('{} nota(s) de R$ {:.2f}'.format(int(num_nota), nota))

print('MOEDAS:')

for moeda in moedas:
    num_moeda = valor // moeda
    valor -= moeda*num_moeda
    print('{} moeda(s) de R$ {:.2f}'.format(int(num_moeda), moeda))
