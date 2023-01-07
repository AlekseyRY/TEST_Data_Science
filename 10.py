'''
Найдите минимум уравнения f(X) = 3*X^3 + 4*X^2 +5*X + 21 на произвольном
интервале с заданной точностью. Напишите функцию на языке “Python” для решения этой
задачи.
'''


def derivative(function):
    f_list = [i for i in function.split(' + ')]
    print(f_list)
    for i in range(len(f_list)):
        if f_list[i] == '3x**3':
            f_list[i] = f_list[i].replace('3x**3', '3*3x**2')
        elif f_list[i] == '4x**2':
            f_list[i] = f_list[i].replace('4x**2', '4*2x')
        elif f_list[i] == '5x':
            f_list[i] = f_list[i].replace('5x', '5')
    f_list.remove('21')
#    print(f_list)
    Der = f_list[0] + '+' + f_list[1] + '+' + f_list[2]
    print(Der)
#    print(type(Der))


    def minimum(function):
        extrPoint = 0
        for x in range(-100, 100):  
            if Der == 0:
                extrPoint = x
        if extrPoint != 0:
            print(extrPoint)
        else:
            print('Точка экстремума не найдена, минимум функции не существует')

    minimum(Der)

F = '3x**3 + 4x**2 + 5x + 21'
derivative(F)
