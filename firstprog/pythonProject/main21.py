#finaaly clause in exception handling
"""Finally Clause
The finally code block is also a part of exception handling.
 When we handle exception using the try and except block,
 we can include a finally block at the end. The finally block is always executed,
 so it is generally used for ,
 doing the concluding tasks like closing file resources or closing database connection
  or may be ending the program execution with a delightful message."""
def func1():
    try:
        l=[1,4,7,9,12]
        print("enter the index:")
        i=int(input())
        print(l[i])
        return 1
    except:
        print("error occurred")
        return 0
    finally:
        print("im always executed")
x=func1()
print(x)