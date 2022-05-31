# print(sum([int(input()) for i in range(2)]))
"""
a, b, c = [int(input()) for i in range(3)]
print(f'{a} {b} {c}')
"""

# print((2222222222)*((888888//444)**2))

"""
Вводится трехзначное число n. Выведите на экран сумму кубов его цифр.
n = int(input())
print((n // 100)**3 + (n // 10 % 10)**3 + (n % 10)**3)

print(sum([int(i)**3 for i in input()]))
"""

s = '1 2 3 5 19'
list_s = list(map(int, s.split()))
index = list_s.index(max(list_s))
print(list_s.index(max(list_s)))
print(sum(map(int, str(max(list_s)))))
