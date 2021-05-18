a =  input("輸入值為:").split(",")

a.sort()
b= list(reversed(a))
x1 =""
x2 =""

for i in range(len(a)):
    x1 = x1+a[i]
    x2 = x2+b[i]
    
print( "最大值數列與最小值數列差值為:",(int(x2)-int(x1)))