#User function Template for python3

class Solution:
    def is_bleak(self, n):
        def count_ones(num):
            count = 0
            while num:
                count += 1
                num &= (num - 1)  # This clears the rightmost 1 bit
            return count
        
        for x in range(max(0, n - 30), n):
            if x + count_ones(x) == n:
                return 0
        return 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_bleak(n)
		print(ans)

# } Driver Code Ends