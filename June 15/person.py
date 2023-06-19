from random import randint 

class Person: 
    balance = 0 
    personal_number = "" 
    birth_date = ""
    first_name = "" 
    last_name = "" 
    ticket = False

    def __init__(self, first_name, last_name, birth_date): 
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.personal_number = randint(100000000000, 999999999999)
        
    def show_info(self): 
        info = f"""Пассажир: {self.first_name} {self.last_name}, \nДата рождения: {self.birth_date}, \nИИН: {self.personal_number}, \nБаланс: {self.balance}$""" 

        print(info)

    def earn(self, amount): 
        self.balance += amount 

    def pay(self, amount): 
        if self.balance >= amount:
            self.balance -= amount 
            return amount 
        return 0

if __name__ == "__main__":  
    print("Person")