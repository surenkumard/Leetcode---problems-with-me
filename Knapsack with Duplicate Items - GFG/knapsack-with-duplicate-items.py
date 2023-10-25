#User function Template for python3

class Solution:
    def knapSack(self, n, w, val, wt):
        arr = [[0 for _ in range(w + 1)] for _ in range(n)]

        for i in range(n):
            for j in range(1, w + 1):
                pick = 0
                np = 0

                if wt[i] <= j:
                    pick = val[i] + arr[i][j - wt[i]]
                if i > 0:
                    np = arr[i - 1][j]

                arr[i][j] = max(pick, np)

        return arr[n - 1][w]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends