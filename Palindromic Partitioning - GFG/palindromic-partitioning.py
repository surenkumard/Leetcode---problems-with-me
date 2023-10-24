#User function Template for python3

class Solution:
    @staticmethod
    def palindromicPartition(string):
        n = len(string)
        arr = [0] * (n + 1)
        arr[0] = 0
        
        for i in range(n):
            minimum = float('inf')
            for j in range(i, -1, -1):
                if Solution.is_palindrome(j, i, string):
                    res = 1 + arr[j]
                    minimum = min(res, minimum)
            arr[i + 1] = minimum
        
        return arr[n] - 1
    
    @staticmethod
    def is_palindrome(i, j, string):
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends