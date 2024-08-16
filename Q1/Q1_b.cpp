#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    auto start = chrono::high_resolution_clock::now();

    int n = 50;
    long long fibo = 0;
    long long fibo1 = 1;
    cout<<0<<" ";

    for(int i=0;i<=n;i++){
        cout<<fibo1<<" ";
        long long temp = fibo1 + fibo;
        fibo = fibo1;
        fibo1 = temp;
    }

    cout<<endl<<endl;

    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = end - start;

    cout<<"Time with Loop: " <<elapsed.count()<<" seconds"<<endl;
    return 0;
}