
#O(n)
#11 passos
def soma1(n):
  soma = 0
  for i in range(n + 1):
    soma += i

  return soma
    
print(soma1(10))

#%timeit soma1(10)
#The slowest run took 6.26 times longer than the fastest.
# This could mean that an intermediate result is being cached.
#1000000 loops, best of 3: 633 ns per loop

#O(3)
#3 passos
def soma(n):
    return(n*(n+1))/2

print(soma(10))

#%timeit soma2(10)
#The slowest run took 13.73 times longer than the fastest.
# This could mean that an intermediate result is being cached.
#10000000 loops, best of 3: 116 ns per loop


#podemos concluir então que o primeiro algoritmo é menos performatico pois para fazer a mesma função
#o primeiro agoritmo leva 11 passos O(11) e a segunda função são feitas em 3 passos O(3)
