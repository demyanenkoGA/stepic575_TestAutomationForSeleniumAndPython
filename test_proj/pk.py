"""
def add_S(*args):
    a = ''
    for arg in args:
        a += arg
    return a


print(add_S('lol', 'kek', '0dd'))
"""


"""
На вход программе подается список целых чисел, разделённых через пробел.

Напишите программу, которая выводит через пробел самое наибольшее отрицательное число и самое наименьшее положительное, либо 0 если какого-либо из них нет.
"""

# dada = lambda stroka: [int(c) for c in stroka.split(' ')]
dada = lambda stroka: list(map(int, stroka.split()))
a1 = '9 8 2 -3 -9 -1'
a2 = '-1 -2 -5 -9'
a3 = '1 4 5'

"""
b = a1.split(' ')
c1 = []
for number in b:
    c1.append(int(number))
print(c1)
"""
ads = dada(a1)
ads.sort()
print(ads)
print(dada(a1))
print(dada(a2))
print(dada(a3))
print(' ')

b = ''
for i in ads:
    if i == 0:
        a = 0
    if i > 0:
        b = i


def value_maxmin(listMin: list = None, listMax: list = None):
    try:
        if listMax:
            return max(filter(lambda y: y < 0, listMax))
        return min(filter(lambda x: x > 0, listMin))
    except ValueError:
        return 0

# print(f'{c[-1]} {c[0]}')
a = map(int, a2.split())
b = map(int, a2.split())
# print(min(filter(lambda x: x > 0, a)))
# print(max(filter(lambda y: y < 0, a)))
m_a = value_maxmin(listMax=a)
m_b = value_maxmin(listMin=b)
print(f'{m_a} {m_b}')

"""
numbers = tuple(map(int, input().split()))

negative_numbers = [number for number in numbers if number < 0]
positive_numbers = [number for number in numbers if number > 0]

max_negative_number = max(negative_numbers) if negative_numbers else 0
min_positive_number = min(positive_numbers) if positive_numbers else 0

print(max_negative_number, min_positive_number)
"""

"""
def test(nums):
    a = [n for n in nums if n > 0]
    b = [n for n in nums if n < 0]
    return [max(b) if b else 0, min(a) if a else 0]


st = list(map(int, input().split()))
print(*test(st))
"""

"""
numbers = input()
numbers = list(filter(lambda x: x.lstrip('-').isdigit(), numbers.split(' ')))
numbers = list(map(int, numbers))

negative = list(filter(lambda x: x < 0, numbers))
positive = list(filter(lambda x: x > 0, numbers))
print(max(negative) if negative else 0, min(positive) if positive else 0)
"""

"""
def get_max_negative_num(numbers: list) -> int:
    negative_nums = [i for i in numbers if i < 0]
    if negative_nums:
        return max(negative_nums)
    return 0


def get_min_positive_num(numbers: list) -> int:
    positive_nums = [i for i in numbers if i > 0]
    if positive_nums:
        return min(positive_nums)
    return 0


if __name__ == '__main__':
    numbers = [int(i) for i in input().split()]
    print(get_max_negative_num(numbers), get_min_positive_num(numbers))
"""
