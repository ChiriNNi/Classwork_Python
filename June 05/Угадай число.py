import random

random_number = random.randint(1, 100)
print(random_number)

def game(attempt=3): 
    attempt -= 1
    user_number = input("Угадай число от 1 до 100: ")

    try: 
        user_number = int(user_number)
    except ValueError: 
        print("Введите целое число!")
        game() 
    else:
        if attempt == 0:
            print("Вы проиграли!")
            return 
        else: 
            if user_number > random_number: 
                print("Введите число поменьше!")
                print(attempt)
            elif user_number< random_number: 
                print("Введите число побольше!")
                print(attempt)
            elif user_number == random_number: 
                print("Вы выиграли!")
                return 
            
            game()
    
game()
    