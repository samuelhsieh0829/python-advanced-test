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

    def methodC(self, arg:int=2):
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

def main():
    obj1 = moduleA(int(input())) #2
    obj2 = moduleA() #default
    for i in range(int(input())): #2
        obj1.methodA()
        obj2.methodA()
    obj1.methodB()
    obj2.methodB()
    obj1.methodC(int(input())) #3
    obj2.methodC() #default

if __name__ == "__main__":
    main()