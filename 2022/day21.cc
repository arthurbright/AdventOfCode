#include <bits/stdc++.h>
#include <iostream>
using namespace std;

ifstream f{"input"};
ifstream ff{"input"};

struct Poly{
    double c;
    double x;
};

int root = -69;
int humn = -69;


const int SIZE = 2049;
vector<int> graph[SIZE];
Poly vals[SIZE];
bool visited[SIZE];


Poly solve(int cur){
    if(visited[cur]) return vals[cur];

    Poly a = solve(graph[cur][0]);
    Poly b = solve(graph[cur][2]);
    double cons = (a.x == 0? a.c: b.c);
    if(graph[cur][1] == 0) return Poly{a.c + b.c, a.x + b.x};
    if(graph[cur][1] == 1) return Poly{a.c - b.c, a.x - b.x};
    if(graph[cur][1] == 2) return Poly{a.c * b.c, (a.x + b.x) * cons};
    if(graph[cur][1] == 3) return Poly{a.c / b.c, (a.x + b.x) / cons};
    throw 0;
}

int main()
{
    //map things (compression)
    map<string, int> mapp;
    string s;
    int cnt = 0;
    while(ff >> s){
        if(s == "root") root = cnt;
        if(s == "humn") humn = cnt;
        mapp[s] = cnt;

        ff >> s;
        try{
            int n = stoi(s);
            visited[cnt] = 1;
            if(humn == cnt){
                vals[cnt] = Poly{0, 1};
            }
            else{
                vals[cnt] = Poly{n, 0};
            }
        }
        catch(...){
            ff >> s;
            ff >> s;
        }

        cnt ++;
    }


    //store the graph
    while(f >> s){
        int cur = mapp[s];
        f >> s;
        try{
            int n = stoi(s);
        }
        catch(...){
            int a = mapp[s];
            graph[cur].push_back(a);
            f >> s;
            if(s == "+") graph[cur].push_back(0);
            else if(s == "-") graph[cur].push_back(1);
            else if(s == "*") graph[cur].push_back(2);
            else if(s == "/") graph[cur].push_back(3);
            else throw 0;

            if(cur == root) graph[cur][1] = 1; //subtract in root

            f >> s;
            graph[cur].push_back(mapp[s]);
        }
    }


    //do topo sort
    for(int i = 0; i < SIZE; i ++){
        vals[i] = solve(i);
        
    }
    cout.precision(30);
    cout << vals[root].c << ", " << vals[root].x << endl;
}
