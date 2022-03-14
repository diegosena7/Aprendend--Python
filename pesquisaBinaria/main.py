
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto:
        meio = (baixo + alto) / 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            alto = meio + 1
        else:
            baixo = meio + 1
        return  None

    my_list = [1, 3, 5, 7, 9]

    print(pesquisa_binaria(my_list, 3))  # => 1

    # 'None' means nil in Python. We use to indicate that the item wasn't found.
    print(pesquisa_binaria(my_list, -1))  # => None