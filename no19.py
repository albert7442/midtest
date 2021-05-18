n=int(input("請輸入組數："))
free=0
list1=[]
for i in range(1,n+1):
    free=0
    a,b = input("第"+str(i)+"組:").split(" ")
    free+=int(a)*250+int(b)*175
    list1.append(free)    
for j in range (1,n+1):
    print("第"+str(j)+"組應收費用:"+str(list1[j-1]),end="\n")