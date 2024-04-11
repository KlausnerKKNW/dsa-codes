def binary_search(array, search_value):
    upper_lim = len(array) - 1
    lower_lim = 0
    midpoint = 0
    global steps
    steps = 0
    while lower_lim <= upper_lim:
        midpoint = (upper_lim + lower_lim)//2
        value_midpoint = array[midpoint]
        steps += 1
        if search_value < value_midpoint:
            upper_lim = midpoint - 1
        if search_value > value_midpoint:
            lower_lim = midpoint + 1
        if search_value == value_midpoint:
            return midpoint
    return 0

array = list()
c = 0
while True:
    array.append(int(input('Digite um valor para colocar na matriz (999 para parar): ')))
    if array[c] == 999:
        array.pop()
        break
    c += 1
value = int(input('Digite um valor para procurar a sua posição na matriz: '))
print(f'O valor desejado está na posição {binary_search(array, value)} da matriz')
print(f'O search foi feito em {steps} passos')



