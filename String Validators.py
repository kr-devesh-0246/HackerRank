if __name__ == '__main__':
    s = input()
    # 5 conditions to check 
    if 0<len(s)<1000:
        # any alpha means atleast one alpha will give true
        # issue:- The loop is running only upto first iteration and then breaks
        # issue:- We need only one True/False after going through all iterations
        # and then if  there contains atleast one condition then True else, false 
        # try to change indentation of if else t/f
        # logic fault : see examples and check there is condition like all the elements satisfy if condition then only it is True, else it will always be False.
        alnum = 0
        for i in s:
            
            if i.isalnum() == True:
                alnum+=1
                
        if alnum!=0:
            print(True)
        else:
            print(False)
        
        alpha = 0
        for i in s:
            
            if i.isalpha() == True:
                alpha+=1
                  
        if alpha!=0:
            print(True)
        else:
            print(False)  
        
        digit = 0
        for i in s:
            
            if i.isdigit() == True:
                digit+=1   
                
        if digit!=0:
            print(True)
        else:
            print(False)
                
        lower = 0
        for i in s:
            
            if i.islower() == True:
                lower+=1   
                
        if lower!=0:
            print(True)
        else:
            print(False)
        
        upper = 0
        for i in s:
            
            if i.isupper() == True:
                upper+=1   
                
        if upper!=0:
            print(True)
        else:
            print(False)
