# Заполните список длины N случайными числами в диапазоне от 0 до 1000
# Выведите:
# 1.длину списка;
# 2.последний элемент списка;
# 3.список в обратном порядке (вспоминаем срезы);
# 4.YES, если список содержит трехзначное число, состоящее из одинаковых цифр
# NO в противном случае;
# 5.список с удаленными первым и последним элементами.


from random import randint
N = int(input())
A=[randint(111,111)
            for i in range(N)]
print(A)
print(len(A))
print(A[N-1])
print(A[::-1])
b = 0
for i in range(N):
    if A[i] in [111,222,333,444,555,666,777,888,999]:
        b +=1
if b ==0:
    print('no')
elif b>0:
    print('yes')
print(A[1:N-1])