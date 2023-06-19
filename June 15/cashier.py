from ticket import Ticket

class Cashier: 
    balance = 0
    tickets = []

    def get_price(self, source, destination): 
        price = (len(source) + len(destination)) * 1000
        return price
    def buy_ticket(self, passenger, source, destination, train): 
        money = passenger.pay(self.get_price(source, destination))
        if money > 0: 
            self.balance += money 
            ticket = Ticket(train.number, source, destination, train.datetime, passenger)
            self.tickets.append(ticket)
            return True 
        else: 
            return False

    def get_ticket(self, passenger, train_id, datetime):
        for item in self.tickets:
            if item.passenger.personal_number == passenger.personal_number and item.train_id == train_id and item.datetime == datetime:
                return item

    def delete_ticket(self, ticket):
        self.tickets.remove(ticket)




if __name__ == "__main__":
    print("Cashier")