#include <bits/stdc++.h>
using namespace std;

long long fibo(long long n,vector<long long> &dp){
    if(n==0 || n==1) return n;
    if(n<0) return 0;

    if(dp[n]!=-1) return dp[n];

    return dp[n] = fibo(n-1,dp) + fibo(n-2,dp);
}

int main(){

    auto start = chrono::high_resolution_clock::now();
    long long n = 50;
    vector<long long> dp(n+1,-1);

    for(long long i=0;i<=n;i++){
        cout<<fibo(i,dp)<<" ";
    }
    cout<<endl<<endl;

    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = end - start;

    cout<<"Time with Recursion and Memoization: " <<elapsed.count()<<" seconds"<<endl;
    return 0;
}