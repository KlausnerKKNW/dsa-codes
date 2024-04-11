from calendar import c


def insertion_sort(array):
    for index in range(1, len(array)):
        temp_value = array[index]
        position = index - 1
        while position >= 0:
            if array[position] > temp_value:
                array[position + 1] = array[position]
                position = position - 1
            else:
                break
        array[position + 1] = temp_value
    return array

org = []
c = 0
while True:
    org.append(int(input('Insira um valor para a lista (999 stop): ')))
    if org[c] == 999:
        org.pop()
        break
    c += 1

print(f'A lista ordenada: {insertion_sort(org)}')

