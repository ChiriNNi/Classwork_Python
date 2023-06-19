from random import randint 

class Train: 
    def __init__(self, cashier, source, destination, datetime):
        self.source = source
        self.destination = destination 
        self.datetime = datetime
        self.number = randint(1, 32)
        self.cashier = cashier

    def go(self, passenger):
        ticket = self.cashier.get_ticket(passenger, self.number, self.datetime)
        if ticket:
            if ticket.train_id == self.number and ticket.datetime == self.datetime:
                print(f"Вы поехали из {self.source} в {self.destination}\nПункт назначения достигнут!")
                self.cashier.delete_ticket(ticket)
            else:
                print("У вас нет билета на данный поезд!")

        
if __name__ == "__main__":  
    print("Train")