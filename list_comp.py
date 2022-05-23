import math
from primalidad import es_primo
list = [ i**2 for i in range(100)]
#print (list)
print("--------")
s = [ n for n in range(101) if n**2-19*n+99 in list  ]
#print(sum(s))
print("--------")
fibo = [1,1]
phi=[]
for i in range(20):
    fibo.append(fibo[-1]+fibo[-2])
    phi.append(float((fibo[i+1]/fibo[i])-(1+math.sqrt(5))/2))

#print(fibo)
print("--------")
#print(phi)
fibo_square = [i for i in fibo if i in list]
print(fibo_square)

primos_fibonacci = [i for i in fibo if es_primo(i)]
print(primos_fibonacci)
 
