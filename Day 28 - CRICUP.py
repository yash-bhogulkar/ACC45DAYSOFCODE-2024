# cook your dish here
for i in range(int(input())):
    x,y,d = map(int,input().split())
    if abs(x-y) <= d:
        print("YES")
    else:
        print('NO')