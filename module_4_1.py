
from fake_math import divide as fake_divide
from true_math import divide as true_divide

if __name__ == '__main__':
    result1 = fake_divide(69, 3)
    result2 = fake_divide(3, 0)
    result3 = true_divide(49, 7)
    result4 = true_divide(15, 0)
    print(f'Деление с делителем не ноль функции divide модуля fake_math: {result1}\n')
    print(f'Деление с делителем ноль функции divide модуля fake_math: {result2}\n')
    print(f'Деление с делителем не ноль функции divide модуля true_math: {result3}\n')
    print(f'Деление с делителем ноль функции divide модуля true_math: {result4}\n')
