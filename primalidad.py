import math
def es_primo(num):
    p= True
    if num in [0,1]:
        p = False
    else: 
        for i in range(2,round(math.sqrt( num) +1)):
            if num % i == 0:
             #print (i, "divide a", num)
             p = False
    return p

def factores_primos (n):
    if es_primo(n):
        L = f"El número {n} es primo"
    elif n == 1:
        L = "Este número no tiene divisores primos "
    elif n == 0:
        L = "Este número tiene infinitos divisores primos "    
    else:
        L = [i for i in range(2,n) if es_primo(i) and n % i == 0]
    
    return L

print (factores_primos(1))
print(es_primo(0))
