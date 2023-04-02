import pandas as pd
import numpy as np


chat_id = 725861714 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    abs_x = np.abs(x - x.mean()) # Вычисляем модуль отклонения от среднего значения
    acceleration = x.mean() / (0.5 * abs_x.mean()) # Вычисляем оценку коэффициента ускорения
    return acceleration
