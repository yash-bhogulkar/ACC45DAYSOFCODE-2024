# cook your dish here
for _ in range(int(input())):
    n,x,p = map(int,input().split())
    if ((x*3) - (n - x)) >= p:
        print('pass')
    else:
        print('fail')
    