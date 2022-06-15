# Enter your code here. Read input from STDIN. Print output to STDOUT

s = str(input())

lower = []; upper = []; evendigit = []; oddigit = []

for i in s:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
    elif i.isdigit():
        if int(i)%2==0:
            evendigit.append(i)
        elif int(i)%2 !=0:
            oddigit.append(i)

sort_lower = sorted(lower); sort_upper = sorted(upper); sort_evendigit = sorted(evendigit); sort_oddigit = sorted(oddigit)
# print(lower, upper, digit)

s_lower = '' 
for i in sort_lower:
    s_lower+=i 
   
s_upper = ''
for i in sort_upper:
    s_upper+=i
    
s_evendigit = ''  
for i in sort_evendigit:
    s_evendigit+=i  

s_oddigit = ''
for i in sort_oddigit:
    s_oddigit+=i
    
print(s_lower+s_upper+s_oddigit+s_evendigit)

        
