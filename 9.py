'''
Существует массив поисковых запросов, например:
search_queries = [“watch new movies", “coffee near me", “how to find the determinant", “python", 
“data science jobs in UK", “courses for data science", “taxi", “google", “yandex", “bing",
"foreign exchange rates USD/BYN", “Netflix movies watch online free", “Statistics courses 
online from top universities"]
Необходимо реализовать функцию, которая принимает на вход данные массива поисковых запросов и 
возвращает распределение поисковых запросов по количеству слов в каждом из запросов в процентах.
Результат должен выглядеть следующим образом:
1 слово : 10%
2 слова:  40%
4 слова:  45%
5 слов:    5%
'''

def raspred(a):
    s = {} #ключ - кол-во слов, значение - кол-во повторений
    for i in range(len(a)):
        n = len(a[i].split()) #кол-во слов в запросе
        if n not in s:
            s[n] = 1
        else:
            s[n] += 1
    print(s)
    m = 0
    for i in s:
        m += s[i]
#    print(m)

    for key in s:
        if key % 10 == 1:
            print(key, ' слово: ', round(s[key] /m * 100),'%', sep = '')
        elif key % 10 == 2 or key % 10 == 3 or key % 10 == 4:
            print(key, ' слова: ', round(s[key] /m * 100),'%', sep = '')
        else:
            print(key, ' слов: ', round(s[key] /m * 100),'%', sep = '')


search_queries = ["watch new movies", "coffee near me", "how to find the determinant", 
"python", "data science jobs in UK", "courses for data science", "taxi", "google", "yandex", 
"bing", "foreign exchange rates USD/BYN", "Netflix movies watch online free", 
"Statistics courses online from top universities"]
raspred(search_queries)