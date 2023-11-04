//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
class Solution
{
public:
    void printPattern(int n)
    {
      for(int k=0;k<(2*n-1);k++){
        int temp = n;
        int i = k;
        i = (i>=n)?(2*n-2-k):k;
        for(int j=0;j< (2*n-1);j++){
            if(i>=j){
                printf("%d",temp);
                temp--;
            }
            else if(i<j && j<=(2*n-2-i)){
                printf("%d",temp+1);
            }
            else{
                temp++;
                printf("%d",temp+1);
            }
          }
        printf("\n");
      }
      // Write Your Code here
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int N;
        cin>>N;
        
        Solution ob;
        ob.printPattern(N);
        
    }
    return 0;
}
// } Driver Code Ends