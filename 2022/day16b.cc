#include <bits/stdc++.h>
#include <iostream>
using namespace std;

vector<int> graphbig [59];
map<int, int> mapp;
int flows[59];

int dist[59][59];

int dp[59][59][32768];
int dp2[59][59][32768];

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

        graphbig[cur].push_back(cur);
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


    //dp[t][x][bitset]  t = time, x = position [0..14], bitset
    for(int time = 1; time <= 26; time ++){
        //build row off prev row
        swap(dp2, dp);
        cout << "Starting iteration " << time << endl;
        memset(dp, 0, sizeof(dp));
        for(int pos = 0; pos < 59; pos ++){
            for(int pos2 = pos; pos2 < 59; pos2 ++){
                for(int bits = 0; bits < 1<<15; bits ++){
                    //dp
                    //move both
                    for(int &next: graphbig[pos]){
                       for(int &next2: graphbig[pos2]){
                            dp[pos][pos2][bits] = max(dp[pos][pos2][bits], dp2[min(next, next2)][max(next, next2)][bits]);
                       }
                    }

                    //press 1, move 2
                    if(flows[pos] && pos < 15 && !(bits & (1 << pos))){
                        for(int &next2: graphbig[pos2]){
                            dp[pos][pos2][bits] = max(dp[pos][pos2][bits], (time - 1) * flows[pos] + dp2[min(pos, next2)][max(pos, next2)][bits | (1 << pos)]);
                        }
                    }

                    //press 2, move 1
                    if(flows[pos2] && pos2 < 15 && !(bits & (1 << pos2))){
                        for(int &next: graphbig[pos]){
                            dp[pos][pos2][bits] = max(dp[pos][pos2][bits], (time - 1) * flows[pos2] + dp2[min(next, pos2)][max(next, pos2)][bits | (1 << pos2)]);
                        }
                    }

                    //press both
                    if(flows[pos] && flows[pos2] && pos != pos2 && pos < 15 && pos2 < 15 && !(bits & (1 << pos)) && !(bits & (1 << pos2))){
                        dp[pos][pos2][bits] = max(dp[pos][pos2][bits], (time - 1) * (flows[pos2] + flows[pos]) + dp2[pos][pos2][bits | (1 << pos2) | (1 << pos)]);
                    }
                }
            }
        }
        cout << dp[15][15][0] << time << endl;
    }

    //go thru neigbours of AA (index 15)

    cout << dp[15][15][0] << endl;
}
