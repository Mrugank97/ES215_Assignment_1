#include <bits/stdc++.h>
#include <chrono>

using namespace std;
using namespace std::chrono;

// Integer type
double matrixInt(int n) {
    vector<vector<int>> A(n,vector<int>(n,1)), B(n,vector<int>(n,1)), result(n,vector<int>(n,0));

    auto start_int = high_resolution_clock::now();

    for(int i = 0;i<n;i++) {
        for(int j = 0;j<n;j++) {
            for(int k = 0;k<n;k++) {
                result[i][j] += A[i][k]*B[k][j];
            }
        }
    }

    auto end_int = high_resolution_clock::now();
    chrono::duration<double> elapsed_int = end_int - start_int;
    cout<<"Time for n = "<<n<<" (Integer & Meat Portion): "<<elapsed_int.count()<<"s"<<"\n";

    return elapsed_int.count();
}



// Double type
double matrixDouble(int n) {
    vector<vector<int>> A(n,vector<int>(n,1.0)), B(n,vector<int>(n,1.0)), result(n,vector<int>(n,0.0));

    auto start_double = high_resolution_clock::now();

    for (int i = 0;i<n;i++) {
        for (int j = 0;j<n;j++) {
            for (int k = 0;k<n;k++) {
                result[i][j] += A[i][k]*B[k][j];
            }
        }
    }

    auto end_double = high_resolution_clock::now();
    chrono::duration<double> elapsed_double = end_double - start_double;
    cout<<"Time for n = "<<n<<" (double & Meat Portion): "<<elapsed_double.count()<<"s"<<"\n";

    return elapsed_double.count();
}


int main() {

    int n;
    cout<<"Enter the Dimension of the Matrix: ";cin>>n;

    auto start_int = high_resolution_clock::now();
    double meat_int = matrixInt(n);
    auto end_int = high_resolution_clock::now();
    chrono::duration<double> elapsed_int = end_int - start_int;
    cout<<"Time for n = "<<n<<" (Integer & Total): "<<elapsed_int.count()<<"s"<<"\n";
    cout<<"Meat Portion exection time w.r.t Total execution time (Integer): "<<(meat_int / elapsed_int.count())*100<<"%"<<"\n";
    cout<<endl;

    auto start_double = high_resolution_clock::now();
    double meat_double = matrixDouble(n);
    auto end_double = high_resolution_clock::now();
    chrono::duration<double> elapsed_double = end_double - start_double;
    cout<<"Time for n = "<<n<<" (double & Total): "<<elapsed_double.count()<<"s"<<"\n";
    cout<<"Meat Portion exection time w.r.t Total execution time (double): "<<(meat_double / elapsed_double.count())*100<<"%"<<"\n";

    return 0;
}
