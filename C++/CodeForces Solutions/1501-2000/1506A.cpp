#include<bits/stdc++.h>
using namespace std;
# define ll long long
int main()
{
    int t;
    cin>>t;
    for(int iterations=0; iterations<t;iterations++)
    {
        ll n, m, x, row, column;
        cin>>n>>m>>x;
        column = x/n;
        //cout<<column<<"\n";
        row = x - (column*n);
        //cout<<row<<"\n";
        if(row==0)
        {
            cout<<((n-1)*m) + column<<"\n"; 
        }
        else
        {
            cout<<((row-1)*m) + column+1<<"\n";
        }
    }
    return 0;
}
