import numpy as np

class VetorOrdenado:

  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, dtype=int)

  # O(n)
  def imprime(self):
    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i])

  # O(n)
  def insere(self, valor):
    #verifica se a capacidade maxima esta atingida
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade atingida')
      return


    posicao = 0
    #percorre a ultima posicao +1
    #encontra a posicao
    for i in range(self.ultima_posicao + 1):
      posicao = i
      if self.valores[i] > valor:
        break
      if i == self.ultima_posicao:
        posicao = i + 1

   #recebe a ultima posicao
    x = self.ultima_posicao
    #algoritimo de remanejamento
    #enquanto x(ultima posicao) for menor ou igual a posicao 
    while x >= posicao:
      self.valores[x + 1] = self.valores[x]
      x -= 1

    self.valores[posicao] = valor
    self.ultima_posicao += 1

  def pesquisa_linear(self, valor):
    for i in range(self.ultima_posicao + 1):
      if self.valores[i] > valor:
        return -1
      if self.valores[i] == valor:
        return i
      

  def pesquisa_binaria(self,valor):
    limite_inferior=0
    limite_superior=self.ultima_posicao

    while True:
      posicao_atual=int((limite_inferior + limite_superior)/2)

      if self.valores[posicao_atual]==valor:
        return posicao_atual
      elif limite_inferior>limite_superior:
        return -1
      else:
        if self.valores[posicao_atual] < valor:
          limite_inferior = posicao_atual +1
        else:
          limite_superior =posicao_atual -1



  def excluir(self, valor):
    posicao = self.pesquisa_binaria(valor)
    if posicao == -1:
      return -1
    else:
      for i in range(posicao, self.ultima_posicao):
        self.valores[i] = self.valores[i + 1]

      self.ultima_posicao -= 1
        

          