a = int(input())
b = int(input())
c = int(input())
n = int(input())
resposta = []

comb = [[x,y,z] for x in range(a+1) for y in range(b+1) for z in range(c+1)]

for i in comb:
    if sum(i) != n:
        resposta.append(i)

print(resposta)