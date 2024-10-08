# cook your dish here
T=int(input())
while T>0:
    X,Y=map(int,input().split())
    print(abs(X-Y))
    T-=1