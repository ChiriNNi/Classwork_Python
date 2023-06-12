class Kettle(): 
    material = "steel"
    color = "red"
    volume = 2.5
    water = 0

    def __init__(self, material, color, volume, water): 
        self.material = material
        self.color = color 
        self.volume = volume
        self.water = water

    def pour(self, liters=None): 
        if liters is None: 
            self.water = self.volume
        elif self.water + liters > self.volume: 
            extra_water = self.water + liters - self.volume
            print(f"Вылилось {round(extra_water, 1)} л. воды!")
            self.water = self.volume
        else:
            self.water += liters
        print("В чайнике", self.water, "л. воды")
    
    def pour_out(self, liters=None): 
        if liters is None: 
            self.water = 0
        elif liters > self.water: 
            extra_water = liters - self.water
            print(f"{round(extra_water, 1)} л. некуда уже выливать!")
            self.water  = 0
        else:
            self.water -= liters
        print("Теперь в чайнике", round(self.water, 1), "л. воды")
    
    def is_hot(self, temperature): 
        if temperature >= 60: 
            print("Осторожно! Чайник горячий!")
        else: 
            print("Не волнуйтесь! Чайник не горячий!")

my_kettle = Kettle("glass", "white", 1.7, 1.7)
# other_kettle = Kettle("wood", "gray", 19)


# my_kettle.pour(0.7)
# my_kettle.pour(0.7)
# my_kettle.pour(0.7)
# my_kettle.pour(0.7)


# my_kettle.pour_out(0.7)
# my_kettle.pour_out(0.7)
# my_kettle.pour_out(0.7)
# my_kettle.pour_out(0.7)

my_kettle.is_hot(100)

