from mod import moduleA
import logging

logging.basicConfig(level=logging.INFO)

def test_normal():
    obj = moduleA(6) # 正常值 1%
    obj.methodA()
    obj.methodB()
    obj.methodC(3)
    return 1

def test_default_value():
    obj1 = moduleA() # 預設值 1%
    obj1.methodA()
    obj1.methodB()
    obj1.methodC()
    return 1

def test_negative():
    obj2 = moduleA(-100) # 負數 3%
    obj2.methodA()
    obj2.methodB()
    obj2.methodC(-69)
    return 3

def test_zero():
    obj3 = moduleA(0) # 0 3%
    obj3.methodA()
    obj3.methodB()
    obj3.methodC(0)
    return 3

def test_float():
    obj4 = moduleA(7.122) # 浮點數 3%
    obj4.methodA()
    obj4.methodB()
    obj4.methodC(8.7)
    return 3

def test_str():
    obj5 = moduleA("WTF") # 字串 3%    
    obj5.methodA()
    obj5.methodB()
    obj5.methodC("WTF")
    return 3

def test_abnormal():
    obj = moduleA(6) # 正常值初始化+不正常的methodC參數+修改count 6%
    obj.methodB()
    obj.methodC(-1) 
    obj.methodC(0)
    obj.methodC(8.29)
    obj.methodC("笑死")
    obj.count = "WTF" #更改屬性 非法count
    obj.methodA()
    return 6

if __name__ == "__main__":
    score = 0

    tests = [test_normal,
             test_default_value, 
             test_negative, 
             test_zero, 
             test_float, 
             test_str, 
             test_abnormal]
    
    for test in tests:
        try:
            score += test()
            logging.info(f"\x1b[32m{test.__name__} pass\x1b[0m")
        except:
            logging.exception(f"\x1b[31m{test.__name__} failed:\x1b[0m")
        finally:
            print("----------------------")

    logging.info(f"\x1b[35mTest completed, score:\x1b[33m{score}\x1b[0m")