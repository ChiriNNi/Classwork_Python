# Person, Ticket, Cashier, Train 

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

class Ticket: 
    number = 0 
    train_id =  0 
    source = "" 
    destination = "" 
    wagon = 0 
    seat = 0
    datetime = "" 
    passenger: Person = False 

    def __init__(self, train_id, source, destination, datetime, person): 
        self.train_id = train_id
        self.source = source
        self.destination = destination
        self.datetime = datetime
        self.passenger = person 
        self.number = randint(100000, 999999) 
        self.wagon = randint(1, 12) 
        self.seat = randint(1, 32)
    
    def show_info(self): 
        info = f"""\nБилет: №{self.number}, \n{self.source} --> {self.destination}, \nОтправление: {self.datetime}, \nПоезд: №{self.train_id}, вагон: {self.wagon}, место: {self.seat}, \nПассажир: {self.passenger.first_name} {self.passenger.last_name}, \nДата рождения: {self.passenger.birth_date}, \nИИН: {self.passenger.personal_number}""" 
        print(info)

class Cashier: 
    balance = 0 

    def get_price(self, source, destination): 
        price = (len(source) + len(destination)) * 1000
        return price
        
    def buy_ticket(self, passenger, source, destination, train): 
        money = passenger.pay(self.get_price(source, destination))
        if money > 0: 
            self.balance += money 
            ticket = Ticket(train.number, source, destination, train.datetime, passenger)
            passenger.ticket = ticket 
            return True 
        else: 
            return False  
        
class Train: 
    source = "" 
    destination = "" 
    datetime = "" 
    number = 0 

    def __init__(self, source, destination, datetime): 
        self.source = source
        self.destination = destination 
        self.datetime = datetime
        self.number = randint(1, 32)

    def go(self, passanger): 
        if passanger.ticket: 
            if passanger.ticket.train_id == self.number and passanger.ticket.datetime == self.datetime: 
                print(f"Вы поехали из {self.source} в {self.destination}\nПункт назначения достигнут!")
            passanger.ticket = False 
    

dude = Person("Ilon", "Mask", "1994-06-25")
dude.earn(25000)
dude.pay(3500)
dude.show_info() 

tmp_ticket = Ticket(0, "Алматы", "Ташкент", "2023-06-16 07:59", dude)

cashier = Cashier() 

tmp_train = Train("Алматы", "Нью-Йорк", "2023-06-16 20:00")
cashier.buy_ticket(dude, "Алматы", "Нью-Йорк", tmp_train)
dude.ticket.show_info() 
tmp_train.go(dude) 

    
