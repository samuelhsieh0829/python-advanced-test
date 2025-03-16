# 寫出符合要求的模組
必須讓以下程式碼可以順利運行:
```py
#app.py
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
```
範例輸出:
```
Module loaded
Module initualized
Module initualized
Hello 0
Hello 1
Hello 0
Hello 1
Hello 2
Hello 3
Hello 4
Hello 0
Hello 1
Hello 0
Hello 1
Hello 2
Hello 3
Hello 4
Count: 4
Count: 10
Count: 4
Count: 4
Count: 4
Count: 10
Count: 10
```
## moduleA
- 此為mod模組中的一個類別
- 將此類別實例化時，可以接收一個參數並儲存為屬性arg
- 初始化另一個屬性count為0
- 透過print出Module initualized表示初始化完成

## moduleA.methodA
- 此為moduleA中第一個方法
- 依照初始化時接受到的參數，print出相同次數的Hello及次數
- 每執行一輪迴圈，一開始初始化的屬性count要+1

## moduleA.methodB
- 此為moduleA中第二個方法
- print出Count及屬性count的數字

## moduleA.methodC
- 此為moduleA中第三個方法
- 需接收一個參數arg
- 執行arg次的methodB

## 通過條件
- 寫出寫出符合條件的moduleA於mod.py，使app.py(最上面的範例程式)可以正常運行 (60%)
- 在其他的環境(非app.py)下引入此模組必須正常運作，不可以有任何報錯(包括但不限於不正常的參數) (40%)

## 知識點
- for迴圈
- 函式
- class
- 自製模組