def linear_search(array, search_value):
    for k, v in enumerate(array):
        if v == search_value:
            return k
        elif v > search_value:
            break
    nada = 'nada'
    
    return nada

print(linear_search((1, 2, 3, 4), 5))
