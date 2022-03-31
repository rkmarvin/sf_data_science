"""Игра угадай число
Компьютер сам загадывает и сам разгадывает число
"""
import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадывает число

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: количество попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return count


def binary_predict(number: int = 1) -> int:
    """Угадывает число алгоритмом бинарного поиска

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: количество попыток
    """
    count = 0
    predict_number = 50
    end = 101
    while True:
        count += 1
        if predict_number == number:
            break
        elif predict_number > number:
            end = predict_number
            predict_number = int(end / 2)
        elif predict_number < number:
            predict_number = predict_number + int((end - predict_number) / 2)
    return count


def score_game(random_predict) -> int:
    """За какое количество в среднем попыток угадываем

    Args:
        random_predict (_type_): _description_

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(
        f'Ваш алгоритм {random_predict.__name__} угадывает '
        f'число в среднем за:{score} попыток'
    )
    return score


if __name__ == '__main__':
    score_game(random_predict)
    score_game(binary_predict)
