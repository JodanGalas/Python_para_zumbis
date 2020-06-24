#03 -

from random import randint
vet01 = []
vet02 = []
vet03 = []
for i in range(10):
    n01 = randint(1, 100)
    vet01.append(n01)
    n02 = randint(1, 100)
    vet02.append(n02)
    vet03.append(vet01[i])
    vet03.append(vet02[i])
print(f'''vetor 01: {vet01}
vetor 02: {vet02}
vetor 03: {vet03}''')