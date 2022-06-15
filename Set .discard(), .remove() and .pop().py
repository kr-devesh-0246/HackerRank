n = int(input())
s = set(map(int, input().split()))

r = int(input())

for i in range(r):
    command = input()
    set_com = command.split()
    
    # play with the data type
    
    if set_com[0] == 'remove':
        s.remove(int(set_com[-1]))
        
    elif set_com[0] == 'pop':
        s.pop()
     
    elif set_com[0] == 'discard':    
        s.discard(int(set_com[-1]))
        
    else:
        pass    
#printing the sum of the elements of the final set 
ans = 0
for i in s:
    ans+=i
    
print(ans)    
       
