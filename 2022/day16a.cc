#include <bits/stdc++.h>
#include <iostream>
using namespace std;

vector<int> graphbig [59];
map<int, int> mapp;
int flows[59];

int dist[59][59];

int dp[31][15][32768];

int enc(char c, char c2){
    return (c - 'A') * 26 + (c2 - 'A');
}

int main()
{

    for(int i = 0; i < 59; i ++){
        for(int j = 0; j < 59; j ++){
            dist[i][j] = INT_MAX;
        }
    }


    ifstream f{"input"};
    ifstream f2{"input"};
    //get map
    string str;
    for(int i = 0; i < 59; i ++){
        getline(f2, str);
        mapp[enc(str[0], str[1])] = i;
    }
    char ch;
    char ch2;
    int flow;

    for(int i = 0; i < 59; i ++){
        f >> ch;
        f >> ch2;
        int cur = mapp[enc(ch, ch2)];
        f >> flow;
        flows[cur] = flow;
        f >> ch;
        f >> ch2;
        graphbig[cur].push_back(mapp[enc(ch, ch2)]);

        while(true){
            f >> ch;
            if(ch != ','){
                f.putback(ch);
                break;
            }
            f >> ch;
            f >> ch2;
            graphbig[cur].push_back(mapp[enc(ch, ch2)]);
        }
    }

    //input done
    //find adjacency for 15 nodes

    for(int start = 0;  start < 15; start ++){
        //bfs from i
        queue<int> todo;
        todo.push(start);
        bool visited[59];
        for(int i = 0; i < 59; i ++) visited[i] = 0;
        visited[start] = 1;
        dist[start][start] = 0;

        while(!todo.empty()){
            int cur = todo.front();
            todo.pop();
            for(int next: graphbig[cur]){
                if(!visited[next]){
                    visited[next] = true;
                    todo.push(next);
                    dist[start][next] = 1 + dist[start][cur];
                    dist[next][start] = 1 + dist[start][cur];
                }
            }

        }
    }

    //first 15 are only that matter
    //bitset on the first 15

    //dp[t][x][bitset]  t = time, x = position [0..14], bitset
    for(int time = 1; time <= 30; time ++){
        //build row off prev row
        for(int pos = 0; pos < 15; pos ++){
            for(int bits = 0; bits < 1<<15; bits ++){
                //dp
                //afk
                dp[time][pos][bits] = dp[time - 1][pos][bits];
                //flip the valve
                if(!(bits & (1 << pos))){
                    dp[time][pos][bits] = max(dp[time][pos][bits], (time - 1) * flows[pos] + dp[time - 1][pos][bits | (1 << pos)]);
                }
                //dont flip the valve
                //go thru all other posses
                for(int pos2 = 0; pos2 < 15; pos2 ++){
                    if(pos2 == pos) continue;
                    //check if we can travel to it in time
                    if(dist[pos][pos2] >= time - 1) continue;
                    int remaintime = time - 1 - dist[pos][pos2];
                    //check bit not set
                    if(!(bits & (1 << pos2))){
                        dp[time][pos][bits] = max(dp[time][pos][bits], remaintime * flows[pos2] + dp[remaintime][pos2][bits | (1 << pos2)]);
                    }
                }
            }
        }
    }

    //go thru neigbours of AA (index 15)

    int maxx = 0;
    for(int i = 0; i < 15; i ++){
        maxx = max(maxx, dp[30 - dist[i][15]][i][0]);
    }

    cout << maxx2 << endl;
}
