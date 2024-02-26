"""Найдите наименьшую обыкновенную дробь, равную вещественному числу 14.375,
и выведите ее на экран в формате '14.375 = числитель/знаменатель'"""

from fractions import Fraction

float_num = 14.375
fraction = Fraction(float_num).limit_denominator()

print(f'{float_num} = {fraction.numerator}/{fraction.denominator}')

