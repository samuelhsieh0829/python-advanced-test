# 寫出符合要求的模組
以下為主程式，本題目目標為寫出moduleA模組的功能，使app.py可以運作
```py
#app.py

# (定義moduleA)

def main():
    obj1 = moduleA(2) #A
    obj2 = moduleA() #預設值
    for i in range(2): #B
        obj1.methodA()
        obj2.methodA()
    obj1.methodB()
    obj2.methodB()
    obj1.methodC(3) #C
    obj2.methodC() #預設值

if __name__ == "__main__":
    main()
```
以上程式之範例輸入:
```
2
2
3
```

範例輸出:
```
Module initialized
Module initialized
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
- 此為一個類別
- 將此類別實例化時，可以接收一個參數並儲存為屬性arg
- 初始化另一個屬性count為0
- 透過print出Module initialized表示初始化完成

## moduleA.methodA
- 此為moduleA中第一個方法
- 依照初始化時接受到的參數，print出相同次數的Hello及次數
- 每執行一輪迴圈，一開始初始化的屬性count要+1

## moduleA.methodB
- 此為moduleA中第二個方法
- print出Count: 及屬性count的數字

## moduleA.methodC
- 此為moduleA中第三個方法
- 需接收一個參數arg
- 執行arg次的methodB

## 測資說明
- 輸入共三行，分別為A、B、C
- A、B、C皆為正整數
- 程式執行流程如app.py，請大家自行從範例輸出中解讀(●'◡'●)

## 通過條件
- 1.可正常接收測資並符合程式需求流程，取得AC (60%)
- 2.寫出符合條件的moduleA，使app.py(最上面的範例程式)可以正常運行 (20%)
- 3.需具有錯誤處理能力，使程式在任何運行環境下(非app.py)不產生任何報錯 (20%)
- 後兩題須使用Python撰寫，讓幹部人工審查
- 4.你的程式寫出來比出題者的AC更AC (100%+🛐⚡)

## 知識點
- for迴圈
- 函式
- class
- 自製模組
- https://slides.com/samuelhsieh/python

## 提示
- 第一題或許只要用簡單的語法就可以了，根本不用管什麼app.py跟moduleA...?
- 第二題請使用Python物件導向功能，製作出正確格式的類別moduleA(而非單純使用流程使程式碼AC)
- 第三題是模擬生產環境應用程式，輸入內容總是不會跟想像中的一樣完美，請檢查好任何變數是否有機會出現意料外的值(非正整數之類的?)，這種東西可以用is_instance()抓出來:O，然後就跟生產環境一樣，在你將程式部屬好前，你都沒辦法知道有可能出什麼問題，沒有測試環境給你除錯(¬‿¬)，所以請盡你所能的寫出你覺得最安全的程式OwO
