#include <bits/stdc++.h>
using namespace std;

int main(){

    auto start = chrono::high_resolution_clock::now();
    long long n = 50;
    vector<long long> dp(n+1,-1);

    dp[0] = 0;
    dp[1] = 1;

    for(long long i=2;i<=50;i++){
        dp[i] = dp[i-1] + dp[i-2];
    }

    for(long long i=0;i<=n;i++){
        cout<<dp[i]<<" ";
    }

    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = end - start;

    cout<<"Time with Loop and Memoization: " <<elapsed.count()<<" seconds"<<endl;
    return 0;
}