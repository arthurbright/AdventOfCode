#include <bits/stdc++.h>
#include <iostream>
using namespace std;

ifstream f{"input"};

struct ele{
    int n;
    queue<ele> arr;

    ele front(){
        return arr.front();
    }
    void poop(){
        arr.pop();
    }
};

ele parseInput(){
    queue<ele> arr;
    char c;
    int inp;

    f >> c;
    if(c >= '0' && c <= '9'){
        f.putback(c);
        f >> inp;
        return ele{inp, queue<ele>()};
    }

    //c = '['
    while(true){
        f >> c;
        if(c == ',') continue;
        if(c != ']'){
            f.putback(c);
            arr.push(parseInput());
        }
        else{
            break;
        }
        
    }
    return ele{-1, arr};
}

int comp(ele a, ele b){
    while(true){
        if(a.n >= 0 && b.n >= 0){
            if(a.n < b.n) return 1;
            if(a.n > b.n) return -1;
            return 0;
        } 

        if(a.n >= 0){
            queue<ele> q;
            q.push(a);
            ele aa = ele{-1, q};
            return comp(aa, b);
        }

        if(b.n >= 0){
            queue<ele> q;
            q.push(b);
            ele bb = ele{-1, q};
            return comp(a, bb);
        }

        //both lists
        //comp first ele
        while(!a.arr.empty() && !b.arr.empty()){
            int r = comp(a.front(), b.front());
            if(r != 0) return r;
            a.poop();
            b.poop();
        }
        if(a.arr.empty() && b.arr.empty()) return 0;
        if(a.arr.empty()) return 1;
        if(b.arr.empty()) return -1;

        
    }
}

int main()
{
    char c;
    int total = 0;
    ele ppp{6, queue<ele>()};
    queue<ele> q;
    q.push(ppp);

    ele pp{-1, q};
    queue<ele> qq;
    qq.push(pp);
    ele p{-1, qq}; //packet

    for(int i = 0; i < 300; i ++){
        ele a = parseInput();

        if(comp(a, p) == 1) total ++;
    }

    cout << total << endl;
}
