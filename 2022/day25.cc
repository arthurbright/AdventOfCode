#include <bits/stdc++.h>
#include <iostream>
using namespace std;

ifstream f{"input"};

long long toD(string str){
    long long tot = 0;
    for(int i = 0; i < str.size(); i ++){
        tot *= 5;
        if(str[i] == '0'){

        }
        else if(str[i] == '1'){
            tot += 1;
        }
        else if(str[i] == '2'){
            tot += 2;
        }
        else if(str[i] == '-'){
            tot --;
        }
        else if(str[i] == '='){
            tot -= 2;
        }
        else{
            throw 1;
        }
    }

    return tot;
}

string back(long long n){
    if(n == 0) return "";
    //find pow 5
    long long k = n % 5;
    if(k > 2) k -= 5;
    n -= k;
    string s;
    if(k == 0) s = "0";
    if(k == 1) s = "1";
    if(k == 2) s = "2";
    if(k == -1) s = '-';
    if(k == -2) s = "=";
    return back(n/5) + s;
}

int main()
{
    string str;
    long long tot = 0;
    while(getline(f, str)){
        tot += toD(str);
       // cout << tot << endl;
    }

    cout << tot << endl;
    cout << back(tot) << endl;


}   
    
