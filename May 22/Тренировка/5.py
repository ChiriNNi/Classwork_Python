hours, minutes, seconds = map(int, input("Введите текущее время (в формате ЧЧ:ММ:СС): ").split(':'))
time_left_seconds = 24 * 60 * 60 - (hours * 60 * 60 + minutes * 60 + seconds)
print(f"До следующего дня осталось {time_left_seconds // 60 // 60}:{time_left_seconds // 60 % 60}:{time_left_seconds % 60}")