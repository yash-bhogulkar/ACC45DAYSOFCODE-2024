# cook your dish here
for t in range(int(input())) :
    x, y=map(int, input().split(' '))
    if(y%x==0) :
        print(y//x -1) 
    else:
        print(y//x)