x = int(input("請輸入一個0~15的整數:"))
a = str(x//8%2) + str(x//4%2) + str(x//2%2) + str(x%2)
b = str(x//8%2) + str(x%8) 
c = str(x%16)

if x < 0 or x > 15:
    print("輸入錯誤")
else:
    if x < 10:
         c = str(x)
    elif x == 10:
         c = "A"
    elif x == 11:
         c = "B"
    elif x == 12:
         c = "C"
    elif x == 13:
         c = "D"
    elif x == 14:
         c = "E"
    elif x == 15:
         c = "F"
    print("二進位:", a)
    print("八進位:", b)
    print("十六進位:", c)