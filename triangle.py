def triangle(n,symbol):
     
    # number of spaces
    k = n - 1    
    for i in range(0, n):
     
        
        for j in range(0, k):
            print(end=" ")
     
        
        k = k - 1
     
        for j in range(0, i+1):
            print(symbol+" ", end="")
             
        print("\r")
 
# Driver Code
n = 5
symbol="#"
triangle(n,symbol)