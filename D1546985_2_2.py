x = int(input())
y = int(input())
s = int(input())

if x not in (0,1) or y not in (0,1) or s not in (0,1):
    print("輸入錯誤")
else:
    if x == 0 and y == 0:
        if s == 0:
            print("第一個閥輸出=0\n允許啟動=0")
        elif s == 1:
            print("第一個閥輸出=0\n允許啟動=0")  
    elif x == 0 and y == 1:
        if s == 0:
            print("第一個閥輸出=1\n允許啟動=0")
        elif s == 1:
            print("第一個閥輸出=1\n允許啟動=1")
    elif x == 1 and y == 0:
        if s == 0:
            print("第一個閥輸出=1\n允許啟動=0")
        elif s == 1:
            print("第一個閥輸出=1\n允許啟動=1")
    elif x == 1 and y == 1:
        if s == 0:
            print("第一個閥輸出=1\n允許啟動=0")
        elif s == 1:
            print("第一個閥輸出=1\n允許啟動=1")                          