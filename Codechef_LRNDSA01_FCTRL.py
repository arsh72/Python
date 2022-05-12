# cook your dish here
t= int(input())
for x in range (t):
    num = int(input())
    count = 0
    while((num//5)>0):
        
        count += num//5
        num = num//5
    print(count)