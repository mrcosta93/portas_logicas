i = 0
entradas = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [1, 1, 1, 1],
]

def porta_not(n1):
    if n1 == 0:
        return 1
    else:
        return 0

def porta_or(n1, n2):
    if n1 == 0 and n2 == 0:
        return 0
    else:
        return 1

def porta_nand(n1, n2):
    if n1 == 0 or n2 == 0:
        return 1
    else:
        return 0

def porta_xnor(n1, n2):
    if n1 == n2:
        return 1
    else:
        return 0

def porta_and(n1, n2):
    if n1 == 1 and n2 == 1:
        return 1
    else:
        return 0



print("----------------")
print("P Q R S  |  W Z")
print("----------------")
while (i < 16):
    a = entradas[i][0]
    b = entradas[i][1]
    c = entradas[i][2]
    d = entradas[i][3]
    resultado1 = porta_not(porta_xnor(porta_nand(porta_or(a, porta_not(b)), porta_not(a)), d))
    resultado2 = porta_xnor(porta_or(porta_and(b, porta_not(c)), c), porta_not(d))
    print(a, b, c, d, " | ", resultado1, resultado2)
    i = i+1
print("---------------")