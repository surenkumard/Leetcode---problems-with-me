#User function Template for python3

class Solution:
    def pattern(self, n):
        # code here
        num = 1
        l = []
        
        for i in range(n,0,-1):
            
            temp = i**2 + num
            result = ""
            
            for _ in range(n-i):
                result += '--'
                
            for _ in range(i):
                result = result + str(num) + '*'
                num += 1
                
            for _ in range(i):
                result = result + str(temp) + '*'
                temp += 1
                
            l.append(result[:len(result) - 1])
            
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.pattern(n)
        for i in range(n):
            print(ans[i])
# } Driver Code Ends