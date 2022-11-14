class User:
    #clase del usuario, info y eso
    def __init__(self):
       self.name = ""
       self.level = 0
       self.Vpoint = 0
    
    def increasePoints(self):
        self.Vpoint += 1
        print("Poinrts Increased")
        print(self.Vpoint)
    
    def establishLevel(self):
        if self.Vpoint <= 4:
            self.level = 1
        elif self.Vpoint <= 7 and self.Vpoint >= 5:
            self.level = 2
        elif self.Vpoint <= 10 and self.Vpoint >= 8:
            self.level = 3
        elif self.Vpoint >= 10:
            self.level = 4
