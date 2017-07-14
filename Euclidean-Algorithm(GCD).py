# Uses python3


import sys

def GCD(a,b):
    
    
    
    if a > b and b !=0:
        r = a % b
        if r == 0:
            return b
        else:
            return GCD(b, r)
  
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
               
            
            
            
            
            
