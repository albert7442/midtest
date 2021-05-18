
do = float(input("請輸入電費度數"))
a = 0  
b = 0

if do <120:
    a = do*2.10
    b = do*2.10
elif do >120 and do <=330:
    a = do*2.10 + (do-120)*3.02
    b = do*2.10 + (do-120)*2.68
elif do >330 and do <=550:
    a = do*2.10 + (do-120)*3.02 + (do-330)*4.39
    b = do*2.10 + (do-120)*2.68 + (do-330)*3.61
elif do >550 and do <=700:
    a = do*2.10 + (do-120)*3.02 + (do-330)*4.39 + (do-550)*4.97
    b = do*2.10 + (do-120)*2.68 + (do-330)*3.61 + (do-550)*4.10
elif do >700:
    a = do*2.10 + (do-120)*3.02 + (do-330)*4.39 + (do-550)*4.97 + (do-700)*5.63
    b = do*2.10 + (do-120)*2.68 + (do-330)*3.61 + (do-550)*4.10 + (do-700)*4.50

print("summer month",a,"non-summer month",b)
