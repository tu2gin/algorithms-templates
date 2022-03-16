# L. Лишняя буква

# Васе очень нравятся задачи про строки, поэтому он придумал свою. 
# Есть 2 строки s и t, состоящие только из строчных букв. Строка 
# t получена перемешиванием букв строки s и добавлением 1 буквы в 
# случайную позицию. Нужно найти добавленную букву.
# Формат ввода

# На вход подаются строки s и t, разделённые переносом строки. 
# Длины строк не превосходят 1000 символов. Строки не бывают пустыми.
# Формат вывода

# Выведите лишнюю букву.

from typing import Tuple

def get_excessive_letter(shorter: str, longer: str) -> str:
    list_1 = list(shorter)
    list_2 = list(longer)
    for i in range(0,len(list_1)):
        if list_1[i] in list_2:
            list_2.remove(str(list_1[i]))
    result = ''.join(list_2)
    return result

def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
