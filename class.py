class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "plays tennis")
        elif self.occupation == "actor":
            print(self.name, "shoot films")
    def speaks(self):
        if self.occupation == "tennis player":
            print(self.name, "I love mission Impossible")
        elif self.occupation == "actor":
            print(self.name, "I love tennis")

tom = Human("Tom cruise", "actor")
tom.do_work()
tom.speaks()

maria = Human("maria sharapova", "tennis player")
maria.do_work()
maria.speaks()