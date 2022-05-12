# cook your dish here
t= int(input())
for x in range(t):
    
    word= input()
    s = len(word)
    if(s%2==0):
    	s1= word[0:s//2]
    	s2= word[s//2:]
    else:
    	s1= word[0: (s//2)]
    	s2= word[(s//2)+1: ]
    l1= list(s1)
    l2= list(s2)
    l1.sort()
    l2.sort()
    s1= str(l1)
    s2= str(l2)
    if(s1==s2):
    	print("YES")
    else:
    	print("NO")
