# cook your dish here
for i in range(int(input())):
    n, a, b = map(int,input().split())
    print(b*(n%2) + (a+b)*(n//2))