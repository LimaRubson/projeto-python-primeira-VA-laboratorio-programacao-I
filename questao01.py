vetor = []

print("################# Sistema de Ordenação Bubble Sort #################")

num = float(input("Digite -1 para sair ou um valor diferente de -1 para ordená-lo: "))
while num != -1: 
    vetor.append(num)
    num = float(input("Digite -1 para sair ou um valor diferente de -1 para ordená-lo: ")) 


def bubble_sort(vet):
     tamanho = len(vet)-1
     for x in range(tamanho):
         #print("Índice x: ", x)
         for y in range(tamanho-x):
             #print("Índice y: ", y)
             if vet[y] > vet[y+1]:
                aux = vet[y]
                vet[y] = vet[y+1]
                vet[y+1] = aux 


if len(vetor) == 0:
    print("Você não digitou nenhum valor para ser ordenado!")
else:   
    print("Valores informados: ", vetor)
    bubble_sort(vetor)
    print("Valores informados de forma ordenada: ", vetor)
