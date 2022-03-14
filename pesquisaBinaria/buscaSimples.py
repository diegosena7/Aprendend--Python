from os import times


def busca_simples(lista_ordenada, elemento_procurado):
    for i, elemento in enumerate(lista_ordenada):
        if elemento == elemento_procurado:
            return i
        else:
            return None

times = ["Santos", "Real Madrid", "Manchester United", "Milan"]
print(busca_simples(times, "Santos"))