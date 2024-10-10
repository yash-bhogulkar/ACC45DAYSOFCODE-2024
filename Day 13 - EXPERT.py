# cook your dish here
T = int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if (2 * Y >= X):
        print("Yes")
    else:
        print("No")