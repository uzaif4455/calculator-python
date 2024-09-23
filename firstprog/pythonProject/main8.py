s = set(map(int, input().split()))
inp = int(input())
res = True
while (inp):
    a = set(map(int, input().split()))
    if len(s) <= len(a):
        res = False
        print(res)
        sys.exit()
    if len(s) > len(a):
        res = s.issuperset(a)
        if not res:
            break
    inp -= 1
print(res)
a = set(input().split())
counter , n = 0, int(input())
for i in range (n):
        b = set(input().split())
        if a.issuperset(b) :
                counter += 1
print(counter == n)
# storage = set(input().split())
# n = int(input())
# output = True
# for i in range(n):
#     storage2 = set(input().split())
#     if not storage2.issubset(storage):
#         output = False
#         if len(storage2) >= len(storage):
#             output = False
# print(output)


