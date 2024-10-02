# cook your dish here
T = int(input())
while T > 0:
    B1, B2, B3 = map(int,input().split())
    if((B1+B2+B3)<2):
        print("Water filling time")
    else:
        print("Not now")
    T-=1