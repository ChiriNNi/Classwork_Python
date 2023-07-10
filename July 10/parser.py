import ini

config = ini.parse('config.ini')
print("Конфигурация:")
print(config)

user_resp = input("Хотите изменить конфигурацию? (yes/no): ")
if user_resp == "yes":
    user_section = input("Введите секцию, который необходимо изменить: ")
    if user_section in config:
        user_key = input("Введите ключ, в котором необходимо изменить: ")
        if user_key in config[user_section]:
            user_in = input("Введите значение, на который необходимо изменить: ")


            if user_in.lower() == 'yes, on, true':
                user_in = True
            elif user_in.lower() == 'no, off, false':
                user_in = False
            elif user_in.isdigit():
                user_in = int(user_in)

            config[user_section][user_key] = user_in

            print(config)
        else:
            print("Данный ключ не найден!")
    else:
        print("Данная секция не найдена!")
