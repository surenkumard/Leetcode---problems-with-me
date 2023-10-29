#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3


class Solution:
    
    #Function to check if Kth bit is set or not.
    def checkKthBit(self, n,k):
        #Your code here
        arr = []
        while(n > 0):
            arr.append(n%2)
            n = n // 2
        
            
        if len(arr) <= k:
            return 0

        
        if arr[k] == 1:
            return 1
        
        return 0
        
        

#{ 
 # Driver Code Starts.


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        k=int(input())
        obj = Solution()
        if obj.checkKthBit(n,k):
            print("Yes")
        else:
            print("No")
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends