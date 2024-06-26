#Constantes são números fixos 1 passo somente ou 2 passos,dependendo do numero de entradas
#Constant - O(1)
lista = [1, 2, 3, 4, 5]

def constants(n):
    print(n[0])
    print(n[1])

constants(lista)


# O tempo de execução aumenta dependendo do numero de n que o usuario define
#Linear O(n)
def linear(n):
  for i in n:
    print(i)

linear(lista)
        

#Um exemplo de uma função quadratica é uma função com 2 laços de repetição
#Quadratic - O(n^2)- polynomial
def quadratic(n):
    for i in n:
        for j in n:
            print(i,j)
        print('---')

quadratic(lista)


#Combination

# O(1) + O(5) + O(n) + O(n) + O(3)
# O(9) + O(2n) -> O(n)

def combination(n):
  # O(1)
  print(n[0])

  # O(5)
  for i in range(5):
    print('test ', i)

  # O(n)
  for i in n:
    print(i)

  # O(n)
  for i in n:
    print(i)

  # O(3)
  print('Python')
  print('Python')
  print('Python')

combination(lista)