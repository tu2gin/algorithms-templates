# D. Хаотичность погоды

# Метеорологическая служба вашего города решила исследовать погоду 
# новым способом. Под температурой воздуха в конкретный день будем 
# понимать максимальную температуру в этот день. Назовём 
# хаотичностью погоды за n дней количество дней, в которые 
# температура строго больше, чем в день до (если такой существует) 
# и в день после текущего (если такой существует). Например, если 
# за 5 дней максимальная температура воздуха составляла [1, 2, 5, 4, 8] 
# градусов, то хаотичность за этот период равна 2: в 3-й и 5-й дни 
# выполнялись описанные условия. Определите по ежедневным показаниям 
# температуры хаотичность погоды за этот период.

# Заметим, что если число показаний n=1, то единственный день будет 
# хаотичным.
# Формат ввода

# В первой строке дано число n –— длина периода измерений в днях, 
# 1 ≤ n≤ 105. Во второй строке даны n целых чисел –— значения 
# температуры в каждый из n дней. Значения температуры не превосходят 
# 273 по модулю.

# Формат вывода

# Выведите единственное число — хаотичность за данный период.

from typing import List

def get_weather_randomness(temperatures: List[int]) -> int:
    n = 0
    len_temp = len(temperatures)
    if len_temp == 1:
        n = 1
        return n
    for i in (range(0,len_temp)):
        if i == 0:
            if temperatures[i+1]<temperatures[i]:
                n = n + 1
        elif i == len(temperatures)-1:
            if temperatures[i-1]<temperatures[i]:
                n = n + 1
        else:
            if ((temperatures[i-1]<temperatures[i])
            and (temperatures[i+1]<temperatures[i])):
                n = n + 1
    return n

def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures

temperatures = read_input()
print(get_weather_randomness(temperatures))

# temp = [-1, -10, -8, 0, 2, 0, 5]
# print(get_weather_randomness(temp))

# temp = [1, 2, 5, 4, 8]
# print(get_weather_randomness(temp))

# temp = [-1, -10, -8, 0, 2, 0, 5]
# print(get_weather_randomness(temp))
