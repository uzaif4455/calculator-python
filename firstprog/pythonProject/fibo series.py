#a=int (input("enter the number : "))
def fibo_seq(n):
    if (n==0 or n==1):
        return n
    else:
        return fibo_seq(n-1)+fibo_seq(n-2)
a=fibo_seq(6)
print(a)
def fibo_seq(n):
    if (n==0 or n==1):
        return n
    else :
        return fibo_seq(n-1)+fibo_seq(n-2)
a=fibo_seq(4)
print(a)
