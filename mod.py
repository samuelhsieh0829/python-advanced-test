class moduleA:
    def __init__(self, arg:int=5):
        self.arg = arg
        self.count = 0
        print("Module initualized")

    def methodA(self):
        for i in range(self.arg):
            print("Hello", i)
            self.count += 1

    def methodB(self):
        print("Count:", self.count)

    def methodC(self, arg:int):
        for i in range(arg):
            self.methodB()
