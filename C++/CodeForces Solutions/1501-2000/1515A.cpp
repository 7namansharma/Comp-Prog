#include<bits/stdc++.h>
using namespace std;
#define ll long long
void solve()
{
    int n, x;
    cin>>n>>x;
    int arr[n];
    ll sum=0;
    //cout<<n<<x;
    for(int i=0;i<n;i++)
    {
        //cout<<i;
        cin>>arr[i];
        sum+=arr[i];
    }
    //cout<<sum<<" "<<x;
    if(sum==x)
    {
        cout<<"NO"<<"\n";
        return;
    }
    else
    {
        sum = 0;
        int temp = 0;
        for(int i=0;i<n;i++)
        {
            if(sum+arr[i]!=x)
            {
                sum += arr[i];
            }
            else
            {
                temp = arr[i];
                arr[i]=arr[i+1];
                arr[i+1] = temp;
                sum += arr[i];
            }
        }
    }
    cout<<"YES"<<"\n";
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<"\n";
    return;
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