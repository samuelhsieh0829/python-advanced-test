from mod import moduleA

def main():
    obj = moduleA(6) # 正常值
    obj1 = moduleA(-100) # 負數 2%
    obj2 = moduleA() # 預設值
    obj3 = moduleA(0) # 0 2%
    obj4 = moduleA(7.122) # 浮點數 2%
    obj5 = moduleA("WTF") # 字串 2%
    for _ in range(2):
        obj.methodA()
        obj1.methodA()
        obj2.methodA()
        obj3.methodA()
        obj4.methodA()
        obj5.methodA()
    obj.methodB()
    obj1.methodB()
    obj2.methodB()
    obj3.methodB()
    obj4.methodB()
    obj5.methodB()
    obj.methodC(3) # 正常值
    obj1.methodC(-69) # 負數 2%
    obj2.methodC() # 預設值
    obj3.methodC(0) # 0 2%
    obj4.methodC(8.7) # 浮點數 2%
    obj5.methodC("WTF") # 字串 2%
    obj.count = "WTF" #更改屬性 非法count 2%
    obj.methodA()

if __name__ == "__main__":
    try:
        main()
        print("Done")
    except Exception as e:
        print(e)
        print("Failed")