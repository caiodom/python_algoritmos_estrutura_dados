from math import log
import numpy as np
import matplotlib.pyplot as plt

n=np.linspace(1,10,100)
print("len",len(n))


print("n.shape",n.shape)

#constant
print(np.ones(n.shape))
print(n)

#Logarithmic
print("np.log(n)",np.log(n))
print(n)

#Linear
print(n)

#Log linear
print("n*n.log(n)",(n*np.log(n)))
print(n)

#Quadratic
print(n**2)
print(n)

#Cubic
print(n**3)
print(n)

#Exponential
print(2**n)
print(n)


labels = ['Constant', 'Logarithmic', 'Linear', 'Log linear', 'Quadratic', 'Cubic', 'Exponential']
big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n**2, n**3, 2**n]

plt.figure(figsize=(10,8))
plt.ylim(0, 100)
for i in range(len(big_o)):
  plt.plot(n, big_o[i], label = labels[i])
plt.legend()
plt.ylabel('Runtime')
plt.xlabel('n')

plt.show()