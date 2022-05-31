from math import sqrt
""""""
"""
a = int(input("Введите число: "))
k = 0
for i in range(2, a // 2+1):
    if (a % i == 0):
        k = k+1
if (k <= 0):
    print("Число простое")
else:
    print("Число не является простым")
"""

"""
ОПЕРАТОР МОРЖА

print(hello := 'world')
print(hello)

print([y for x in [1, 2, 5] if (y := sqrt(x)) < 10])
"""

"""
Через логику
a, b = int(input()), int(input())
print((a, b)[a > b])

Через функцию min()
print(min(int(input()), int(input())))

С помощью оператора моржа
print(((a := int(input())), (b := int(input())))[a > b])
"""

data = [i for i in range(0, 10) if i % 2 is 0]
print(data)
