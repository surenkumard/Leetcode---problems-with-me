//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++
#include <string.h> 

void toBinary(int n)
{
    // your code here
    string str = "";
    while(n > 0){
        str = to_string((n % 2)) + str;
        n = n / 2;
    }
    
    cout << str;
    
}

//{ Driver Code Starts.

int main() {
	//code
	
	int t;
	cin>>t;
	
	
	while(t--)
	{
	    int n;
	    cin>>n;
	    
	    toBinary(n);
	    cout<<endl;
	}
	return 0;
}
// } Driver Code Ends