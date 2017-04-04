import random

class Coin :
    def __init__(self, clean = True, rare = False, heads = True, **kwargs) :
        self.is_clean = clean
        self.is_rare = rare
        self.is_heads = heads

        for key,value in kwargs.items() :
            setattr(self, key, value)
        
        if self.is_rare :
            self.value = self.original_value * 1.5
        else :
            self.value = self.original_value

        if self.is_clean :
            self.color = self.original_color
        else :
            self.color = self.rusty_color

    def clean(self) :
        self.color = self.original_color

    def rust(self) :
        self.color = self.rusty_color

    def flip(self) :
        self.is_heads = random.choice([True, False])

    def __del__(self) :
        print("Spent {} !".format(self))

    def __str__(self) :
        return "Coin of value {}, of color {}, is rare {}, heads ? {}".format(self.value, self.color, self.is_rare, self.is_heads)


class Ten_Rupee(Coin) :
    def __init__(self) :
        data = {
            "original_value" : 10.00,
            "rusty_color" : "GREEN",
            "original_color" : "GOLD"
        }
        super().__init__(**data)

class One_Rupee(Coin) :
    def __init__(self) :
        data = {
            "original_value" : 1.00,
            "rusty_color" : "SILVER",
            "original_color" : "SILVER"
        }
        super().__init__(**data)

    # override 
    def rust(self) :
        self.color = self.original_color

class Fifty_Paisa(Coin) :
    def __init__(self) :
        data = {
            "original_value" : 0.50,
            "rusty_color" : "WHITE",
            "original_color" : "YELLOW"
        }
        super().__init__(clean = False, rare = True, **data)


#create coins, rust, clean, flip, print

myTenRupee = Ten_Rupee()
print(myTenRupee)
myTenRupee.rust()
myTenRupee.flip()
print(myTenRupee)

myRupee = One_Rupee()
print(myRupee)
myRupee.rust()
myRupee.flip()
print(myRupee)

myFiftyPaise = Fifty_Paisa()
print(myFiftyPaise)
myFiftyPaise.clean()
myFiftyPaise.flip()
print(myFiftyPaise)

del myRupee
del myFiftyPaise
del myTenRupee


