#include<bits/stdc++.h>
using namespace std;
#define ll long long
void solve()
{
    int n, k1, k2, w, b;
    cin>>n>>k1>>k2;
    cin>>w>>b;
    w-=min(k1, k2);
    b-=(n-max(k1,k2));
    w-=abs(k1-k2)/2;
    b-=abs(k1-k2)/2;
    if(w<=0 && b<=0)
    {
        cout<<"YES"<<"\n";
    }
    else
    {
        cout<<"NO"<<"\n";
    }
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        solve();
    }
}