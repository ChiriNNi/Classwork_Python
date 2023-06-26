input_data = input("Введите элементы массива, через запятую: ")
nums = list(map(int, input_data.split(",")))
count = 0 
counts = []
for i in range(len(nums)-1): 
    if nums[i] <= nums[i+1]: 
        count += 1 
    else: 
        count = 0 
print(max(counts))




























