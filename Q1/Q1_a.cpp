#include <bits/stdc++.h>
using namespace std;
#include <ctime>
#include <iostream>

long long fibo(long long n){
    if(n==0 || n==1) return n;
    if(n<0) return 0;
    else return fibo(n-1) + fibo(n-2);
}

int main(){    

    auto start = chrono::high_resolution_clock::now();
    long long n = 50;
    for(int i=0;i<=n;i++){
        cout<<fibo(i)<<" ";
    }

    cout<<endl<<endl;

    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = end - start;

    cout<<"Time with Recursion: " <<elapsed.count()<<" seconds"<<endl;
    return 0;
}