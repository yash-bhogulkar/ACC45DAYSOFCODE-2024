# cook your dish here
for i in range(int(input())):
    n = int(input())
    
    even, odd = 0,0
    for i in range(1, n+1):
        if n%i == 0:
            if i%2 == 0:
                even += 1
            
            else:
                odd += 1
                
    if even<odd:
        print(-1)
    elif even>odd:
        print(1)
    else:
        print(0)