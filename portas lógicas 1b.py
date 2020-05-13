i = 0
entrada = [
    [0, 0], 
    [0, 1], 
    [1, 0], 
    [1, 1]
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

print("---------")
print("A B  |  X")
print("---------")
while(i < 4):
    a = entrada[i][0]
    b = entrada[i][1]
    resultado = porta_or(porta_and(porta_not(a), b), porta_and(porta_not(b), a))
    print(a, b, " | ", resultado)
    i = i+1
print("----------")