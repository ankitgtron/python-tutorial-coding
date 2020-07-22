class Father():
    def skills(self):
        print("gardening, coding")
class Mother():
    def skills(self):
        print("cooking, art")
class Child(Father, Mother):
    def skills(self):
        print("Sports")
        Father.skills(self)
        Mother.skills(self)

c = Child()
c.skills()





