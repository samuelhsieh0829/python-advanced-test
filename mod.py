print("Module loaded")
class moduleA:
    def __init__(self, arg:int=5):
        self.arg = arg
        self.count = 0
        if self.check_arg(arg) == False:
            print("arg is not int")
            return
        if arg <= 0:
            print("arg is less than 1")
            return
        print("Module initualized")

    def methodA(self):
        if self.check_arg(self.arg) == False:
            print("arg is not int")
            return
        if self.arg <= 0:
            print("arg is less than 1")
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
            print("arg is not int")
            return
        if arg <= 0:
            print("arg is less than 1")
            return
        for i in range(arg):
            self.methodB()

    def check_arg(self, arg):
        if isinstance(arg, int) == False:
            return False
        return True
