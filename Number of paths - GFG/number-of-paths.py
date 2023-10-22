#User function Template for python3
class Solution:
    mod = 1000000007

    def numberOfPaths(self, M, N):
        n = M + N - 2
        r = min(M - 1, N - 1)
        res = 1

        for i in range(1, r + 1):
            res = (res * (n - r + i) % self.mod * self.modInverse(i, self.mod)) % self.mod

        return res

    def modInverse(self, a, b):
        x = 1
        y = 0
        while a > 1:
            q = a // b
            temp = b
            b = a % b
            a = temp
            temp = y
            y = x - q * y
            x = temp

        return x + self.mod if x < 0 else x



#{ 
 # Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        M, N = map(int, input().split())
        ans = ob.numberOfPaths(M, N)
        print(ans)




# } Driver Code Ends