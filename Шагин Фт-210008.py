from statistics import geometric_mean
number = int(input('Введите количество критериев (целое число): '))
matrix = []  # матрица для данных сравнения критериев
for i in range(number):   # циклы для ввода данных сравнения критериев
    line = []  # строка матрицы
    for j in range(number):
        if i == j: # сравнение одинаковых критериев
            a = 1
        elif i > j: # повторная (лишняя) попытка сравнения
            a = 1 / matrix[j][i]  # ввод обратного числа в матрицу
        else:
            while True:     # цикл обработки ввода данных сравнения критерия
                try:
                    a = float(input(f'Введите отношение критерия {i + 1} к критерию {j + 1}: '))
                    break
                except:
                    print ('Ошибка ')
        line.append(a)   # добавление критерия
    matrix.append(line)  # добавление строки в матрицу
s = 0   # сумма средних геометрических значений
SRZ = []   # список средних геометрических значений
for c in range(number): # заполнение списка средних геометрических значений
    Sr = geometric_mean(matrix[c])  # вычисление среднего геометрического
    s += Sr
    SRZ.append(Sr)
for l in range(number):    # цикл вывода весового коэффициента критериев
    weight = SRZ[l] / s
    print (f'Весовой коэффициент {l + 1} критерия: {round(weight, 2)}')
