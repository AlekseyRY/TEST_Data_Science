'''
Реализуйте функцию принимающую 2 аргумента - 2-е даты. Результатом вычисления функции должна 
быть разница между 2-й датой и 1-й датов в днях. В случае если разница принимает негативное 
значение вывести в консоль абсолютное значение разницы в днях. Используем стандартный модуль 
Python для работы с датами datetime (без внешних библиотек).
'''
import datetime

def dates(a, b):
#    print(a)
#    print(b)
    c = b - a 
#    d = c.days
    if c >= datetime.timedelta(days = 0):
        print(c.days)
    else:
        print(-c.days)


#date1 = datetime.datetime(2022, 10, 20)
#date2 = datetime.datetime(2022, 10, 5)

#dates(date1, date2)