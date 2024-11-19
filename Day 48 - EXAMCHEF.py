# cook your dish here
for i in range(int(input())):
    x,y,z=map(int,input().split())
    a=x*y
    b=a/2
    if b<z: print("YES")
    else: print("NO")