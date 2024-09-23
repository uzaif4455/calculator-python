# enter the number8
# 40.0
# 8*1 = 8 it is less40.0
# 8*2 = 16 it is less40.0
# 8*3 = 24 it is less40.0
# 8*4 = 32 it is less40.0
# 8*5 = 40 it is equal40.0
# 8*6 = 48 it is greater40.0
# 8*7 = 56 it is greater40.0
# 8*8 = 64 it is greater40.0
# 8*9 = 72 it is greater40.0
# 8*10 = 80 it is greater40.0
# 8*11 = 88 it is greater40.0
#
# Process finished with exit code 0

a=int(input("enter the number:"))
avg=(a*10)/2
for i in range(1,11):

    if (a*i)<(avg):
        print(f"{a}","x",i,"=",(a*i),f" it is less then: {avg}")
    elif (a*i)==(avg):
        print(f"{a}", "x", i, "=", (a * i), f" it is equal: {avg}")
    elif (a*i)>(avg):
        print(f"{a}", "x", i, "=", (a * i), f" it is greater then: {avg}")

