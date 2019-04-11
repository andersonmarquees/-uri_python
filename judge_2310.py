n = int(input())
saque, block, attack, total_saque, total_block, total_attack = 0, 0, 0, 0, 0, 0
saque_acept, block_acept, attack_acept, total_acept = 0, 0, 0, 0
while n > 0:

    name = input()
    data = list(map(int, input().split()))
    saque += data[0]
    block += data[1]
    attack += data[2]

    data_acert = list(map(int, input().split()))
    saque_acept += data_acert[0]
    block_acept += data_acert[1]
    attack_acept += data_acert[2]
    n -= 1

total_saque = (saque_acept * 100) / saque
total_block = (block_acept * 100) / block
total_attack = (attack_acept * 100) / attack
print("Pontos de Saque: {:.2f} %.".format(total_saque))
print("Pontos de Bloqueio: {:.2f} %.".format(total_block))
print("Pontos de Ataque: {:.2f} %.".format(total_attack))


