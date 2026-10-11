x = int(input())
y = int(input())

if x not in (0,1) or y not in (0,1):
    print("輸入錯誤")
else:
    if x == 0 and y == 0 :
        print("OR=0\nAND=0\nXOR=0")
    elif x == 0 and y == 1 :
        print("OR=1\nAND=0\nXOR=1")
    elif x == 1 and y == 0 :
        print("OR=1\nAND=0\nXOR=1")
    elif x == 1 and y == 1 :
        print("OR=1\nAND=1\nXOR=0")        