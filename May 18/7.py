hours, minutes = map(int, input("Введите часы и минуты: ").split())
day = hours * 60 + minutes 
ost_day = 1440 - day 
ost_hours = ost_day // 60
print(f"Осталось {ost_hours} часов и {ost_day - (ost_hours * 60)}")