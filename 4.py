'''
Напишите функцию, на вход которой подается матрица Mn,m. Функция должна провести операцию 
транспонирования для полученной матрицы, вывести результат в консоль и вывести размерность для 
исходной и транспонированной матрицы.
'''

def transpose(M: list[list[int]]):
	trans_M = [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
	print(trans_M)
	print("Исходная матрица:", len(M),'x', len(M[0]), "Транспонированная:", len(trans_M), 'x', len(trans_M[0]))

test = [[1, 2, 3], [2, 3, 4], [7, 7, 7], [8, 8, 8]]
transpose(test)