# cook your dish here
for t in range(int(input())):
    a,b,c =map(int,input().split())
    if(b>=a and b>=c):
        print("yes")
    else:
        print("no")