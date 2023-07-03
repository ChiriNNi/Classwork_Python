file = open("./task_2.txt", encoding="utf-8")

# 1
def formated_text(array, length):
    for i in range(len(array)):
        words = array[i].split()
        result = ""
        count = 0

        for word in words:
            if count + len(word) <= length:
                result += word + " "
                count += len(word) + 1
            else:
                result += "\n" + word + " "
                count = len(word) + 1
        array[i] = result
    return array


array = file.readlines()
length = int(input("Максимальная длина строки: "))

print(formated_text(array, length))

file.close()