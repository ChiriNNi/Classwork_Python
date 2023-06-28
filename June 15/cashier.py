from ticket import Ticket

class Cashier:
    balance = 0
    tickets = []
    trains = []

    def get_price(self, source, destination):
        price = (len(source) + len(destination)) * 1000
        return price

    def register_train(self, train):
        self.trains.append(train)

    def buy_ticket(self, passenger, source, destination):
        suitable_trains = []
        for train in self.trains:
            if train.source == source and train.destination == destination:
                suitable_trains.append(train)

        if len(suitable_trains) > 0:
            money = passenger.pay(self.get_price(source, destination))
            if money > 0:
                self.balance += money
                chosen_train = suitable_trains[0]  # Выбираем первый подходящий поезд
                ticket = Ticket(chosen_train.number, source, destination, chosen_train.datetime, passenger)
                self.tickets.append(ticket)
                print(f"--- Билет на поезд {chosen_train.number} от {source} до {destination} успешно куплен.")
            else:
                print("--- У пассажира недостаточно средств для покупки билета.")
        else:
            print(f"--- Нет подходящих поездов от {source} до {destination}. Билет не может быть куплен.")

    def get_ticket(self, passenger, train_id, datetime):
        for item in self.tickets:
            if item.passenger.personal_number == passenger.personal_number and item.train_id == train_id and item.datetime == datetime:
                return item

    def delete_ticket(self, ticket):
        self.tickets.remove(ticket)


if __name__ == "__main__":
    print("Cashier")