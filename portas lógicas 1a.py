i = 0
entradas = [
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 1], 
    [0, 0, 0, 1, 0], 
    [0, 0, 0, 1, 1], 
    [0, 0, 1, 0, 0], 
    [0, 0, 1, 0, 1], 
    [0, 0, 1, 1, 0], 
    [0, 0, 1, 1, 1], 
    [0, 1, 0, 0, 0], 
    [0, 1, 0, 0, 1], 
    [0, 1, 0, 1, 0], 
    [0, 1, 0, 1, 1], 
    [0, 1, 1, 0, 0], 
    [0, 1, 1, 0, 1], 
    [0, 1, 1, 1, 0], 
    [0, 1, 1, 1, 1], 
    [1, 0, 0, 0, 0], 
    [1, 0, 0, 0, 1], 
    [1, 0, 0, 1, 0], 
    [1, 0, 0, 1, 1], 
    [1, 0, 1, 0, 0], 
    [1, 0, 1, 0, 1], 
    [1, 0, 1, 1, 0], 
    [1, 0, 1, 1, 1], 
    [1, 1, 0, 0, 0], 
    [1, 1, 0, 0, 1], 
    [1, 1, 0, 1, 0], 
    [1, 1, 0, 1, 1], 
    [1, 1, 1, 0, 0], 
    [1, 1, 1, 0, 1], 
    [1, 1, 1, 1, 0], 
    [1, 1, 1, 1, 1]
]

def porta_nand(n1, n2):
    if n1 == 0 or n2 == 0:
        return 1
    else:
        return 0

def porta_and(n1, n2):
    if n1 == 1 and n2 == 1:
        return 1
    else:
        return 0

def porta_or(n1, n2):
    if n1 == 0 and n2 == 0:
        return 0
    else:
        return 1

def porta_xnor(n1, n2):
    if n1 == n2:
        return 1
    else:
        return 0

print("----------------")
print("A B C D E  |  X")
print("----------------")
while (i < 32):
    a = entradas[i][0]
    b = entradas[i][1]
    c = entradas[i][2]
    d = entradas[i][3]
    e = entradas[i][4]
    resultado = porta_xnor(porta_or(porta_and(porta_nand(a, b), c), d), e)
    print(a, b, c, d, e, " | ", resultado)
    i = i+1
print("----------------")