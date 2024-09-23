#hacker rank questions
"""import numpy as np
np.set_printoptions(legacy="1.13")

arr = np.array(input().split(), float)

print(np.floor(arr), np.ceil(arr), np.rint(arr), sep="\n")"""
import numpy

"""# Step 1: Read input dimensions
N, M = map(int, input().split())

# Step 2: Read the matrix
A = numpy.array([input().split() for _ in range(N)], int)

# Step 3: Compute the sum of each column
column_sums = numpy.sum(A, axis=0)

# Step 4: Compute the product of the column sums
product_of_sums = numpy.prod(column_sums, axis=0)

# Step 5: Print the result
print(product_of_sums)"""
"""x=int(input())
y=int(input())
z=int(input())
n = int(input())
list = []
for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            if i + j + k != n:
                list.append([i, j, k])
            print(list)"""
#find the runner upscore
"""if __name__ == '__main__':
    i = int(input())
    l1 = list(map(int))[:i]#,.strip().split()))[:i]
    z = max(l1)
    while max(l1) == z:
        l1.remove(max(l1))

    print max(l1)"""
#method 2
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     result=sorted(set(arr))[-2]
#     print(result)
#nested list question
"""if __name__ == '__main__':
    N = int(input())
    students = []
    for i in range(N):
        name = input()
        grade = float(input())
        students.append([name, grade])

    grades = set([grade for name, grade in students])
    sorted_grades = sorted(grades)
    second_lowest_grade = sorted_grades[1]

    second_lowest_students = [name for name, grade in students if grade == second_lowest_grade]

    second_lowest_students.sort()
    for student in second_lowest_students:
        print
"""
#finding the average:percentage
#if__name__==__main__:
N=input()
student_marks={}
for i in range(N):
    data=input().split()
    name=data[0]
    marks=list(map(float,data[1:]))
    student_marks[name]=marks   #ASSIGNING KEY:VALUE

query_name=input()      #TAKING INPUT FOR NAME
marks=student_marks[query_name]  #TAKING VALUE FROM INPUT KEY
average=sum(marks)/len(marks)
print(f"{average:.2f}")

