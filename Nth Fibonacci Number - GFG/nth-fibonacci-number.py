
class Solution:
    def nthFibonacci(self, n : int) -> int:
        # code here
        if n <= 1:
            return n
        
        a = 0
        b = 1
        for _ in range(2, n+1):
            a, b = b, (a + b) % 1000000007
        
        return b
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends