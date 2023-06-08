import random
import time 

print(" " * 55 + "-- Угадай число --")


def game(random_number, min_value, max_value, attempts, attempts_left = 0):
    if attempts == 0:
        print("Вы проиграли! А число было:", random_number)
        time.sleep(1)
        return
    
    print("--- Осталось", attempts, "попыток.")

    user_number = input("Угадай число от %s до %s: " % (min_value, max_value))
    print()
    attempts_left += 1
    
    try:
        user_number = int(user_number)
    except ValueError:
        print("Введите целое число!")
        game(random_number, min_value, max_value, attempts_left)
        return

    if random_number < user_number:
        print("-- Введите число меньше ;)\n")
    elif random_number > user_number:
        print("-- Введите число больше :)\n")
    else:
        print("Правильно! Вы угадали за", attempts_left, "попыток.")
        time.sleep(1)
        return

    game(random_number, min_value, max_value, attempts - 1, attempts_left)


def play_game():
    print("\nНастройка игры:\n")
    min_value_input = input("Введите минимальное значение диапазона: ")
    max_value_input = input("Введите максимальное значение диапазона: ")


    try:
        min_value = int(min_value_input)
        max_value = int(max_value_input)
    except ValueError:
        print("Введите целочисленные значения!")
        play_game()
        return

    random_number = random.randint(min_value, max_value)
    attempts = 7

    print("\nИгра начинается!\n")
    time.sleep(1)

    game(random_number, min_value, max_value, attempts)

    play_again = input("Хотите ещё раз сыграть (да/нет)? ")
    if play_again.lower() in "да / д / yes / y":
        play_game()


play_game()