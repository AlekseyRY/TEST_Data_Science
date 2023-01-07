'''
Игральную кость бросили N раз. Какова вероятность того, что M раз выпадет число не менее S. 
Напишите функцию на языке Python для решения данной задачи, для любых N, M и S. Вывести 
результат в консоль.
'''
def probability(n: int, m: int, s: int):
    if n < m:
        print('Число бросков должно быть не меньше, чем число вероятностей события')
    else: 
        def faktorial(t):
            if t == 0:
                return 1
            return (faktorial(t - 1) * t)
        
        p = (7 - s) / 6

        P = (faktorial(n)/(faktorial(m) * faktorial(n-m))) * p**m * (1 - p)**(n - m)
        print(P)


N = 10
M = 4
S = 3

probability(N, M, S)

