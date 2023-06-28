from random import randint 
from person import Person 

class Ticket:
    number = 0
    train_id = 0
    source = ""
    destination = ""
    wagon = 0
    seat = 0
    datetime = ""
    passenger = None

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

    def __repr__(self):
        info = f"Билет №{self.number} {self.source} --> {self.destination} на поезде №{self.train_id} в {self.datetime}"
        return info
    
    # "Магический" метод __eq__, сравнивает билеты по их номеру
    def __eq__(self, other):
        return self.number == other.number 
    
if __name__ == "__main__":  
    print("Ticket")