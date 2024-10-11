# cook your dish here
for T in range(int(input())):
    a,b,c,d = map(int,input().split())
    print(max((a,b)) + max((c,d)))

