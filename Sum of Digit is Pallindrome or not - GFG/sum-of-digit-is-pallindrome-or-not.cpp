//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int isDigitSumPalindrome(int n) {
        int sum1;
        int temp;
        
        while(n > 0){
            temp = n % 10;
            n = n / 10;
            sum1 += temp; 
        }
        
        temp = sum1;
        
        int sum2 = 0;
        while(temp > 0){
            int last_dig = temp % 10;
            temp /= 10;
            sum2 = sum2 * 10 + last_dig;    
        }
        if (sum2 == sum1){
            return 1;
        }
        return 0;
        
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;
        Solution ob;
        cout << ob.isDigitSumPalindrome(N) << "\n";
    }
}

// } Driver Code Ends