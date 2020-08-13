import random 
class Mobile :
    screen_size = 5
    battery = 4100
    os = "Android"

samsung = Mobile()
print("Samsung", samsung.screen_size)
print("Samsung", samsung.battery)
print("Samsung", samsung.os)

redmi = Mobile()
print("RedMi", redmi.screen_size)
print("RedMi", redmi.battery)
print("RedMi", redmi.os)

samsung.screen_size = 4.5
print("Samsung", samsung.screen_size) # 4.5
print("RedMi", redmi.screen_size) # 5


class MyCoin :
    def __init__(self, rare = False) :
        self.rare = rare
        if rare :
            self.value = 1.5
        else :
            self.value = 1
        self.edges = 0
        self.color = "GOLD"
        self.is_heads = True

    def __del__(self) :
        print("Coin well spent!")

    def rust(self) :
        self.color = "GREEN"

    def clean(self) :
        self.color = "GOLD"

    def flip(self) :
        self.is_heads = random.choice([True, False])

    def paint(self, color) :
        self.color = color


rupee = MyCoin()
print(rupee.rare, rupee.value, rupee.color, "Is heads : {}".format(rupee.is_heads))
rupee.flip()
print("Is heads : {}".format(rupee.is_heads))
rupee.flip()
print("Is heads : {}".format(rupee.is_heads))

rupee.rust()
print(rupee.color)

rupee.clean()
print(rupee.color)

rupee.paint("BLACK")
print(rupee.color)

del rupee

pound = MyCoin(True)
print(pound.rare, pound.value, pound.color, "Is heads : {}".format(pound.is_heads))
