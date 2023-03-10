'''
Напишите функцию, которая принимает на вход два вектора (2 списка) и рассчитывает косинусное 
расстояние полученных векторов и выводит результат вычисления в консоль. Реализуйте проверку 
для валидности расчета косинусного расстояния между 2-мя векторами, в случае если проверка не 
прошла, вывести в консоль причину почему рассчитать расстояние между 2-мя векторами невозможно.
'''

def cos_rasst(a: list[int], b:list[int]) -> float:
    if len(a) != len(b):
        print("Ошибка! Размерность векторов должна быть одинаковой")
    else:
        def skalar(c, d): #скалярное произведение
            skl = 0
            for i in range(len(a)):
                skl += c[i] * d[i]
            return skl


        def modul(e): #длина (модуль) векторов
            mod = 0
            for i in range(len(a)):
                mod += e[i] ** 2
            return mod ** 0.5

        cs = skalar(a, b) / (modul(a) * modul(b))
        print(cs)


vect_1 = [1, 4, 7, 17]
vect_2 = [8, 17, -5, 20]

cos_rasst(vect_1, vect_2)
