#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        # code here
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        n = len(S)
        value = roman[S[n-1]]
        for i in range(n-2,-1,-1):
            current = roman[S[i]]
            temp = roman[S[i+1]]
            
            if temp > current:
                value -= current
            else:
                value += current
                
        return value
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends