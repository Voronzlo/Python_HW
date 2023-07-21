# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать
# сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

# Получение числителя и знаменателя
def getting_numbers(string):
    numerator, denominator = map(int, string.split('/'))
    return numerator, denominator

# Сложение двух дробей
def add_fractions(fraction1, fraction2):
    numerator_1, denominator_1 = fraction1
    numerator_2, denominator_2 = fraction2
    result_numerator = numerator_1 * denominator_2 + numerator_2 * denominator_1
    result_denominator = denominator_1 * denominator_2
    return result_numerator, result_denominator

# Перемножение двух дробей
def multiply_fractions(fraction1, fraction2):
    numerator1, denominator1 = fraction1
    numerator2, denominator2 = fraction2
    result_numerator = numerator1 * numerator2
    result_denominator = denominator1 * denominator2
    return result_numerator, result_denominator

# Нахождение наибольшего общего делителя
def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Сокращение дроби 
def shorten_the_fraction(fraction):
    numerator, denominator = fraction
    common_divisor = greatest_common_divisor(numerator, denominator)
    reduced_numerator = numerator // common_divisor
    reduced_denominator = denominator // common_divisor
    return reduced_numerator, reduced_denominator


if __name__ == "__main__":
  # Ввод дробей
	string_1 = input("\n1. Введите первую дробь в формате a/b: ")
	string_2 = input("2. Введите вторую дробь в формате a/b: ")

	# Извлечение числителя и знаменателя
	extracting_number_1 = getting_numbers(string_1)
	extracting_number_2 = getting_numbers(string_2)

	# Вывод итогового рузультат сложения двух дробей
	adding_fractions = add_fractions(extracting_number_1, extracting_number_2)
	reduced_adding_fractions = shorten_the_fraction(adding_fractions)
	print("\n1. Сумма дробей:", '/'.join(map(str, reduced_adding_fractions)))

	# Вывод итогового рузультат перемножения двух дробей
	mult_fractions = multiply_fractions(extracting_number_1, extracting_number_2)
	reduced_mult_fractions = shorten_the_fraction(mult_fractions)
	print("2. Произведение дробей:", '/'.join(map(str, reduced_mult_fractions)))

	# Проверка своего кода при помощи модуля fractions
	print(f'\n1. Проверка результата первой дроби при помощи fractions: {Fraction(string_1) + Fraction(string_2)}')
	print(f'2. Проверка результата второй дроби при помощи fractions: {Fraction(string_1) * Fraction(string_2)}')