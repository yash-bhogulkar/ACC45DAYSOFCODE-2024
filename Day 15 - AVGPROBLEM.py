# cook your dish here
T = int(input())
for i in range (T):
    a, b, c =  map(int,input().split())
    if (a + b)/2 > c:
        print("Yes")
    else:
        print("No")