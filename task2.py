# Заполните массив длины N случайными числами в интервале [0,5].
# Определить, есть ли в нем элементы с одинаковыми значениями, стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 7
# [1, 2, 3, 3, 2, 2, 1]
# Вывод:
# значение:3 индексы 2 и 3
# значение:2 индексы 4 и 5
from random import randint
N = int(input())
A=[randint(0,5)
            for i in range(N)]
print(A)
b=0
for i in range(N-1):
    if A[i]==A[i+1]:
        print("yes",i , i+1)
        b+=1
if b ==0:
    print('no')