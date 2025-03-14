class moduleA:
    def __init__(self, arg:int=5):
        if self.check_arg(arg) == False:
            print("Invalid argument")
            return
        self.arg = arg
        self.count = 0
        print("Module initualized")

    def methodA(self):
        if self.check_arg(self.arg) == False:
            print("Invalid argument")
            return
        if self.check_arg(self.count) == False:
            print("Invalid count")
            return
        for i in range(self.arg):
            print("Hello", i)
            self.count += 1

    def methodB(self):
        print("Count:", self.count)

    def methodC(self, arg:int):
        if self.check_arg(arg) == False:
            print("Invalid argument")
            return
        for i in range(arg):
            self.methodB()

    def check_arg(self, arg):
        if isinstance(arg, int) == False:
            return False
        if arg <= 0:
            return False
        return True
