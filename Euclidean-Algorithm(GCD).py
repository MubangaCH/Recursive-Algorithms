# Uses python3


import sys
# a and b are two integers
def GCD(a,b):
    
    
    
    if a > b and b !=0:
        r = a % b           #r is the remainder when a (or b) is divided by b (or a)
        if r == 0:
            return b
        else:
            return GCD(b, r) # uses b and r as the next arguments for the function
  
    if b > a and a != 0:
        r= b % a
        
        if r == 0:
            return a
        else:
            return GCD(a, r)
    
    if a==b and b !=0:
        return a
    
    if b==0 and a != 0:
        return a   
    if a==0 and b != 0:
        return b   
       
    
if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(GCD(a, b))     
               
            
            
            
            
            
