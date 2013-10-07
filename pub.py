class Customer:

    def __init__(self):
        self.glass = None

    def buy_beer(self, beer_type= "pint"):
        if beer_type == "half":
            self.glass = Glass(10)
        elif beer_type == "pint":
            self.glass = Glass(20)
        elif beer_type == "triple":
            self.glass = Glass(60)
        else:
            raise ValueError("We don't serve that here")

    def drink(self):
        self.glass.drink(1)

    def quaff(self):
        self.glass.drink(4)

    def down_in_one(self):
        self.glass.drink()


class Glass:
    def __init__(self, content=20):
        self.content = content
    
    def drink(self, ounces = None):
        if ounces is None:
            ounces = self.content
        if self.content - ounces < 0:
            self.content = 0
            raise Exception(self.content)
        self.content -= ounces

    def __bool__(self):
        return bool(self.content)


