i = 0
entrada1 = [
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

entrada2 = [
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

def porta_not(n1):
    if n1 == 0:
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

#Questão A
print("Letra A:")
print("-------------")
print("A B C D  |  X")
print("-------------")
while (i < 16):
    a1 = entrada1[i][0]
    b1 = entrada1[i][1]
    c1 = entrada1[i][2]
    d1 = entrada1[i][3]
    resultadoA = porta_or(porta_and(a1, b1), porta_and(c1, d1))
    print(a1, b1, c1, d1, " | ", resultadoA)
    i = i+1
print("-------------")
i = 0

#Questão B

print("Letra B:")
print("-------------")
print("A B C D  |  X")
print("-------------")
while (i < 16):
    a2 = entrada1[i][0]
    b2 = entrada1[i][1]
    c2 = entrada1[i][2]
    d2 = entrada1[i][3]
    resultadoB = porta_and(porta_or(a2, b2), porta_or(c2, d2))
    print(a2, b2, c2, d2, " | ", resultadoB)
    i = i+1
print("-------------")
i = 0

#Questão C

print("Letra C:")
print("----------------")
print("A B C D E  |  X")
print("----------------")
while (i < 32):
    a3 = entrada2[i][0]
    b3 = entrada2[i][1]
    c3 = entrada2[i][2]
    d3 = entrada2[i][3]
    e3 = entrada2[i][4]
    resultadoC = porta_not(porta_and(a3, porta_or(b3, porta_not(porta_and(porta_or(d3, e3), c3)))))
    print(a3, b3, c3, d3, e3, " | ", resultadoC)
    i = i+1
print("----------------")