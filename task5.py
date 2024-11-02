# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.

N = int(input())
a=[]
k = 0
for i in range(N):
    b = int(input())
    a.append(b)
M = 0
for d in range(N):
    if M<a[d]:
        M = a[d]
        k = 0
    if M ==a[d]:
        k+=1
print(k)