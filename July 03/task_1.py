file = open("./task_1.txt", encoding="utf-8")
array = [row.strip() for row in file]
print(array)
original_word = input("Введите исходное слово: ")
new_word = input("Введите новое слово: ")
for i in range(len(array)):
    if original_word.title() in array[i]:
        result = array[i].replace(original_word.title(), new_word.title())
    if original_word.lower() in array[i]:
        result = array[i].replace(original_word.lower(), new_word.lower())
    if original_word.upper() in array[i]:
        result = array[i].replace(original_word.upper(), new_word.upper())
    print(result)
file.close()
