from my_package import numbers, strings

#numbers:

first_num = float(input("Введите первое число: "))
second_num = float(input("Введите второе число: "))

Sum = numbers.plus(first_num, second_num)
Multiply = numbers.mult(first_num, second_num)
Power = numbers.power(first_num, second_num)

print("Сумма чисел равна: ", Sum)
print("Произведение чисел равно: ", Multiply)
print("Первое число в степени второго равно: ", Power)

#strings:

content = input("Введите текст: ")

Upper = strings.upper(content)
Reverse = strings.reverse(content)
Space_Remover = strings.space_remover(content)

print("Высокий регистр: ", Upper)
print("Задом наперёд: ", Reverse)
print("Без пробелов: ", Space_Remover)




