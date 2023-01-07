'''
Написать функцию на языке Python, аргументом которой является целочисленный массив (список, 
элементами которого является тип данных int). Функция должна обработать целочисленный массив 
и вернуть только уникальные значения (без дубликатов)  для данного массива c сортировкой по 
возрастанию.
'''

def unique(array: list[int]) -> list[int]:
    result = []
    for element in array:
        if element not in result:
            result.append(element)
    result.sort()
#    print(result)
    return result


test = [11, 2, 3, 41, 5, 2, 3, 5, 7, 12, 5, 3]
unique(test)