//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    string isSquare(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4) {
        // code here
        int dis1, dis2, dis3, dis4;
        dis1 = sqrt(pow(x2-x1, 2) + pow(y2-y1, 2));
        dis2 = sqrt(pow(x3-x2, 2) + pow(y3-y2, 2));
        dis3 = sqrt(pow(x4-x3, 2) + pow(y4-y3, 2));
        dis4 = sqrt(pow(x1-x4, 2) + pow(y1-y4, 2));
        
        if(dis1 == dis3 && dis2 == dis4 && dis1 != 0 ){
            return "Yes";
        }
        return "No";
        
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int x1, y1, x2, y2, x3, y3, x4, y4;
        
        cin>>x1>>y1>>x2>>y2>>x3>>y3>>x4>>y4;

        Solution ob;
        cout << ob.isSquare(x1,y1,x2,y2,x3,y3,x4,y4) << endl;
    }
    return 0;
}
// } Driver Code Ends