# Массив имеет четное число элементов N.
# Заполнить массив случайными числами и
# выполнить реверс отдельно в первой половине и второй половине.
# Пример: ввод N = 6
# [1,2,3,4,5,6]
# Вывод: [3,2,1,6,5,4]


from random import randint
N = int(input())
A=[randint(1,N)
        for i in range(N)]
print(A)
B =[0:N/2]

