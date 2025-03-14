import mod

def main():
    obj1 = mod.moduleA(2)
    obj2 = mod.moduleA()
    for i in range(2):
        obj1.methodA()
        obj2.methodA()
    obj1.methodB()
    obj2.methodB()
    obj1.methodC(3)
    obj2.methodC(2)

if __name__ == "__main__":
    main()
