# cook your dish here
def working_hours():
    X,Y = map(int,input().split())
    print(4*X+Y)
    
T = int(input())
while (T > 0):
    T = T - 1
    working_hours()