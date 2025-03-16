import mod

def main():
    obj = mod.moduleA(6) # 正常值
    obj1 = mod.moduleA(-100) # 負數
    obj2 = mod.moduleA() # 預設值
    obj3 = mod.moduleA(0) # 0
    obj4 = mod.moduleA(0.5) # 浮點數
    obj5 = mod.moduleA("WTF") # 字串
    for i in range(2):
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
    obj1.methodC(-69) # 負數
    # obj2.methodC() # 無參數
    obj3.methodC(0) # 0
    obj4.methodC(0.5) # 浮點數
    obj5.methodC("WTF") # 字串
    obj.count = "WTF" #更改屬性 非法count
    obj.methodA()

if __name__ == "__main__":
    try:
        main()
        print("Done")
    except Exception as e:
        print(e)
        print("Failed")