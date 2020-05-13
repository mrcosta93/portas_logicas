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

def porta_or(n1, n2, n3, n4):
    if n1 == n2 == n3 == n4 == 0:
        return 0
    else:
        return 1

def porta_and(n1, n2, n3, n4):
    if n1 == n2 == n3 == n4 == 1:
        return 1
    else:
        return 0

print("-------------")
print("A B C D  |  X")
print("-------------")
while (i < 16):
    a = entradas[i][0]
    b = entradas[i][1]
    c = entradas[i][2]
    d = entradas[i][3]
    resultado = porta_and(porta_or(a, b, c, porta_not(d)), porta_or(a, b, porta_not(c), d), porta_or(porta_not(a), porta_not(b), c, porta_not(d)), porta_or(porta_not(a), porta_not(b), porta_not(c), d))
    print(a, b, c, d, " | ", resultado)
    i = i+1
print("-------------")


