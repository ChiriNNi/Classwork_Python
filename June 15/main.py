# Person, Ticket, Cashier, Train
from person import Person
from ticket import Ticket
from cashier import Cashier
from train import Train

if __name__ == "__main__":
    ilon = Person("Ilon", "Mask", "1994-06-25")
    ilon.earn(95000)
    ilon.show_info()

    alex = Person("Alex", "Dough", "1994-06-25")
    alex.earn(85000)

    cashier = Cashier()

    train_to_chile = Train(cashier, "Алматы", "Сантьяго", "2023-06-16 20:00")
    train_to_uruguay = Train(cashier, "Алматы", "Монтевидео", "2023-06-26 09:00")


    cashier.buy_ticket(ilon, "Алматы", "Сантьяго", train_to_chile)
    cashier.buy_ticket(ilon, "Алматы", "Монтевидео", train_to_uruguay)

    cashier.buy_ticket(alex, "Алматы", "Сантьяго", train_to_chile)
    cashier.buy_ticket(alex, "Алматы", "Норильск", train_to_chile)

    print(cashier.tickets)
    train_to_chile.go(ilon)
    print(cashier.tickets)


