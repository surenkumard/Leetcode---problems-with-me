#User function Template for python3

class Solution:
    def minimumNumberOfDeletions(self,S):
        # code here 
        n = len(S)
        arr = [[0] * (n + 1) for _ in range(n + 1)]
        s = S[::-1]

        for i in range(n, -1, -1):
            for j in range(n, -1, -1):
                if i == n or j == n:
                    arr[i][j] = 0
                elif S[i] == s[j]:
                    arr[i][j] = 1 + arr[i + 1][j + 1]
                else:
                    arr[i][j] = max(arr[i][j + 1], arr[i + 1][j])

        return n - arr[0][0]


        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()

        ob = Solution()
        print(ob.minimumNumberOfDeletions(S))
# } Driver Code Ends