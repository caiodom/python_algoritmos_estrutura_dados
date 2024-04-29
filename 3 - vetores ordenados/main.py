from vetor import VetorOrdenado
import random


vetor=VetorOrdenado(10)
vetor.imprime()
print("\n")

vetor.insere(6)
vetor.imprime()
print("\n")

vetor.insere(4)
vetor.imprime()
print("\n")

vetor.insere(3)
vetor.imprime()
print("\n")

vetor.insere(5)
vetor.imprime()
print("\n")

vetor.insere(1)
vetor.imprime()
print("\n")

vetor.insere(8)
vetor.imprime()
print("\n")


vetor.insere(2)
vetor.imprime()
print("\n")

vetor.insere(9)
vetor.imprime()
print("\n")

print("\n Pesquisando 8")
print(vetor.pesquisa_linear(8))


print("\n Pesquisando 2")
print(vetor.pesquisa_linear(2))

print("\n Pesquisando 9")
print(vetor.pesquisa_linear(9))

print("\n excluindo 1 - 2")
vetor.excluir(1)
vetor.imprime()


print("\n Pesquisando 8 Binaria")
print(vetor.pesquisa_binaria(8))


print("\n Pesquisando 2 Binaria")
print(vetor.pesquisa_binaria(2))

print("\n Pesquisando 9 Binaria")
print(vetor.pesquisa_binaria(9))


