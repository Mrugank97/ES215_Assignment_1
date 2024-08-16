#include <bits/stdc++.h>
#include <chrono>

using namespace std;
using namespace std::chrono;

// Integer type
vector<vector<int>> matrixInt(int n) {
    vector<vector<int>> A(n,vector<int>(n,1)), B(n,vector<int>(n,1)), result(n,vector<int>(n,0));

    for(int i = 0;i<n;i++) {
        for(int j = 0;j<n;j++) {
            for(int k = 0;k<n;k++) {
                result[i][j] += A[i][k]*B[k][j];
            }
        }
    }

    return result;
}



// Double type
vector<vector<int>> matrixDouble(int n) {
    vector<vector<int>> A(n,vector<int>(n,1.0)), B(n,vector<int>(n,1.0)), result(n,vector<int>(n,0.0));

    for (int i = 0;i<n;i++) {
        for (int j = 0;j<n;j++) {
            for (int k = 0;k<n;k++) {
                result[i][j] += A[i][k]*B[k][j];
            }
        }
    }

    return result;
}


int main() {

    int n;
    cout<<"Enter the Dimension of the Matrix: ";cin>>n;

    auto start_int = high_resolution_clock::now();
    auto result_int = matrixInt(n);
    auto end_int = high_resolution_clock::now();
    chrono::duration<double> elapsed_int = end_int - start_int;
    cout<<"Time for n = "<<n<<" (Integer): "<<elapsed_int.count()<<"s"<<"\n";


    auto start_double = high_resolution_clock::now();
    auto result_double = matrixDouble(n);
    auto end_double = high_resolution_clock::now();
    chrono::duration<double> elapsed_double = end_double - start_double;
    cout<<"Time for n = "<<n<<" (double): "<<elapsed_double.count()<<"s"<<"\n";

    return 0;
}
