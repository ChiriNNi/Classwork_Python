# Person, Ticket, Cashier, Train
from person import Person
from ticket import Ticket
from cashier import Cashier
from train import Train

if __name__ == "__main__":
    # Создаем экземпляры классов Person, Cashier и Train
    ilon = Person("Ilon", "Mask", "1994-06-25")
    ilon.earn(95000)
    ilon.show_info()

    alex = Person("Alex", "Dough", "1994-06-25")
    alex.earn(85000)

    cashier = Cashier()

    train_to_chile = Train(cashier, "Алматы", "Сантьяго", "2023-06-16 20:00")
    train_to_uruguay = Train(cashier, "Алматы", "Монтевидео", "2023-06-26 09:00")

    # Покупка билетов
    # * случай, где получается купить билет на подходящий поезд
    cashier.buy_ticket(ilon, "Алматы", "Сантьяго")
    cashier.buy_ticket(ilon, "Алматы", "Монтевидео")

    # * случай, где нет подходящего поезда и билет купить нельзя
    cashier.buy_ticket(alex, "Алматы", "Нью-Йорк")
    cashier.buy_ticket(alex, "Алматы", "Рим")

    print()
    print(cashier.tickets)
    train_to_chile.go(ilon)
    print(cashier.tickets)

    # "Магические" методы
    print("\nДемонстрация работы магических методов:")
    person = Person("John", "Doe", "1990-01-01")
    print("Магический метод __repr__:", repr(person))

    first_ticket = Ticket(12345, "Алматы", "Нур-Султан", "2023-07-01", person)
    second_ticket = Ticket(54321, "Алматы", "Алматы", "2023-07-02", person)
    print("Магический метод __eq__:", first_ticket == second_ticket)

    train = Train(cashier, "Алматы", "Нур-Султан", "2023-07-01 08:00")
    print("Магический метод __str__:", train)


