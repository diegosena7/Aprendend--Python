def busca_binaria(lista_ordenada, elemento_procurado):
    primeiro_elemento_lista, ultimo_elemento_lista = 0, len(lista_ordenada) - 1

    while primeiro_elemento_lista <= ultimo_elemento_lista:
        meio = (primeiro_elemento_lista + ultimo_elemento_lista) // 2

        if lista_ordenada[meio] == elemento_procurado:
            return meio
        elif lista_ordenada[meio] > elemento_procurado:
            ultimo_elemento_lista = meio - 1
        else:
            primeiro_elemento_lista = meio + 1

    return None


print(busca_binaria([0, 3, 5, 7, 9], 7))
print(busca_binaria([0, 3, 5, 7, 9], 3))

# Busca Binária #
# Em uma lista ordenada buscamos um elemento X na lista e retornamos a posição deste elemento
# Criamos 2 variáveis para receber o primeiro elemento da lista (seria a posição 0), o último elemento da lista
# recebe a posição final da lista -1
# Percorremos a lista enquanto o primeiro elemento da lista for menor ou igual ao último elemento da lista
# Nessa condição a posição meio da lista recebe o valor da variável primeiro elemento + último elemento / 2
# Se o meio da lista for == elemento procurado eu retorno a posição do elemento (meio)
# Se o meio da lista for > elemento procurado o último elemento recebe o meio da lista - 1
# na condição acima descrita significa que o  elemento procurado está na parte inferior da lista
# se não significa que o elemento prcurado está na parte superior da lista e nessa condição o primeiro elemento
# recebe o meio da lista + 1
