class Solution:
    def gfSeries(self, N : int) -> None:
        # code here
        a = [0, 1]
        for i in range(2,N):
            num = (a[i-2] ** 2) - (a[i - 1])
            a.append(num)
        for i in range(N):
            print(a[i], end = " ")
        print()
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        obj = Solution()
        obj.gfSeries(N)

# } Driver Code Ends