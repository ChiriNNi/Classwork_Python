hours, minutes = map(int, input("Введите текущее время (в формате ЧЧ:ММ): ").split(':'))
current_minutes = hours * 60 + minutes
minutes_per_day = 24 * 60
time_left_minutes = minutes_per_day - current_minutes
print(f"До следующего дня осталось {time_left_minutes // 60}:{time_left_minutes % 60}")
