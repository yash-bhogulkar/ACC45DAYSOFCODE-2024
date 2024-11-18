# cook your dish here
for i in range(int(input())):
    n,x=map(int,input().split())
    x=x%n
    if(x==0):
        print("YES")
    else:
        print("NO")