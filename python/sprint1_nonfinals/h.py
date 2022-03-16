# H. Двоичная система

# Тимофей спросил у Гоши, умеет ли тот работать с числами в 
# двоичной системе счисления. Он ответил, что проходил это на 
# одной из первых лекций по информатике. Тимофей предложил Гоше 
# решить задачку. Два числа записаны в двоичной системе счисления. 
# Нужно вывести их сумму, также в двоичной системе. Встроенную 
# в язык программирования возможность сложения двоичных чисел 
# применять нельзя.

# Решение должно работать за O(N), где N –— количество разрядов
#  максимального числа на входе.
# Формат ввода

# Два числа в двоичной системе счисления, каждое на отдельной 
# строке. Длина каждого числа не превосходит 10 000 символов.

# Формат вывода

# Одно число в двоичной системе счисления.


from typing import Tuple

def to_binary(number: int) -> str:
    result = ''
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    return result

def get_sum(first_number: str, second_number: str) -> str:
    sum = int(first_number, 2) + int(second_number, 2)
    result = to_binary(sum)
    return result

def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))
