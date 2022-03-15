from turtle import rt
from typing import List

def get_weather_randomness(temperatures: List[int]) -> int:
    # Здесь реализация вашего решения
    for i in (range(1,(len(temperatures))-1)):
        if result == '':
            if ((temperatures[i-1]<temperatures[i])
                or (temperatures[i+1]<temperatures[i])):
                result = i
    return result

def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures

temperatures = read_input()
print(get_weather_randomness(temperatures))
