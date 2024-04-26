from vetor import VetorNaoOrdenado



vnp= VetorNaoOrdenado(5)

print(vnp.imprime())

vnp.insere(2)
print(vnp.imprime())

vnp.insere(3)
vnp.insere(5)
vnp.insere(8)
vnp.insere(1)

print(vnp.imprime())

vnp.insere(7)
print(vnp.imprime())

print("pesquisa 8 posição: ",vnp.pesquisar(8))

print("pesquisa 9 posição: ",vnp.pesquisar(9))

print("última posição: ",vnp.ultima_posicao)

print(vnp.imprime())


vnp.excluir(1)
print(vnp.imprime())

vnp.excluir(2)
print(vnp.imprime())

vnp.insere(5)
vnp.insere(1)
vnp.imprime()