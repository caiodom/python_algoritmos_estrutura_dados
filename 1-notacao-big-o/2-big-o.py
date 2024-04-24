#O(1000)->O(n)
def lista1():
    lista=[]
    for i in range(1000):
        lista+=[i]
    return lista

print(lista1())    
print(len(lista1()))

#%timeit lista1()
#10000 loops, best of 3: 68.3 µs per loop

def lista2():
    return range(1000)

l=lista2()

for i in l:
    print(i)

#%timeit lista2()
#The slowest run took 9.26 times longer than the fastest. 
#This could mean that an intermediate result is being cached.
#1000000 loops, best of 3: 270 ns per loop
