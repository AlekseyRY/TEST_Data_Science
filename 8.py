'''
Напишите функцию, на вход которой подается массив распределения из n случайных чисел 
(желательно, чтобы количество случайных целочисленных значений в массиве было больше 100).
Функция должна рассчитать для массива меры центральной тенденции (среднее, моду и медиану) 
и вывести значения в консоль.
Также необходимо вывести результат, является ли распределение случайных чисел симметричным 
или асимметричным (без расчета коэффициента асимметрии, используя лишь меры центральной 
тенденции).
'''

def tendency(a):
    summ = 0
    for i in a:
        summ += i
        srednee = summ / len(a)
    print('Среднее:', srednee)

    t = len(a) / 2
#    print(t)
    a.sort()
#    print(a)
    if len(a) % 2 == 0:
        mediana = (a[int(t - 1)] + a[int(t)]) / 2
    elif len(a) % 2 != 0:
        mediana = a[int(t)]
    print('Медиана:', mediana)

    count = {}
    for i in a:
        if i not in count:
            count[i] = 1
        else:
            count[i] +=1
#    print(count)
    moda = 0
    for i in count:
        if count[i] > moda:
            moda = i
    print('Мода:', moda)

    if srednee == mediana and mediana == moda:
        print('Это симметричное распределение')
    else: 
        print('Это несимметричное распределение')


test = [7, 1, 2, 4, 15, 22, 41, 2, 7, 30, 44, 3, 8, 77, 7, 15, 20, 2, 50, 7, 20, 100, 7]
tendency(test)