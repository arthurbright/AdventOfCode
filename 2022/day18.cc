#include <bits/stdc++.h>
#include <iostream>
using namespace std;

ifstream f{"input"};

bool grid[201][201][201];
bool visited[201][201][201];

struct Trip{
    int x;
    int y;
    int z;
};

int main()
{
    int a, b, c;
    for(int i = 0; i < 2741; i ++){
        f >> a >> b >> c;
        a ++;
        b ++;
        c ++;

        grid[a][b][c] = 1;
        //cout << a << endl;
    }

    //bfs from outside
    queue<Trip> todo;

    for(int i = 0; i < 201; i ++){
        for(int j = 0; j < 201; j ++){
            visited[0][i][j] = 1;
            visited[i][0][j] = 1;
            visited[i][j][0] = 1;
            visited[i][j][200] = 1;
            visited[i][200][j] = 1;
            visited[200][i][j] = 1;
            todo.push(Trip{0, i, j});
            todo.push(Trip{i, 0, j});
            todo.push(Trip{i, j, 0});
            todo.push(Trip{200, i, j});
            todo.push(Trip{i, 200, j});
            todo.push(Trip{i, j, 200});
        }
    }

    int x, y, z;
    while(!todo.empty()){
        Trip cur = todo.front();
        todo.pop();
        x = cur.x;
        y = cur.y;
        z = cur.z;

        if(x < 200 && !visited[x + 1][y][z] && !grid[x + 1][y][z]){
            visited[x + 1][y][z] = 1;
            todo.push(Trip{x + 1, y, z});
        }
        if(y < 200 && !visited[x][y + 1][z] && !grid[x][y + 1][z]){
            visited[x][y + 1][z] = 1;
            todo.push(Trip{x, y + 1, z});
        }
        if(z < 200 && !visited[x][y][z + 1] && !grid[x][y][z + 1]){
            visited[x][y][z + 1] = 1;
            todo.push(Trip{x, y, z + 1});
        }
        if(x > 0 && !visited[x - 1][y][z] && !grid[x - 1][y][z]){
            visited[x - 1][y][z] = 1;
            todo.push(Trip{x - 1, y, z});
        }
        if(y > 0 && !visited[x][y - 1][z] && !grid[x][y - 1][z]){
            visited[x][y - 1][z] = 1;
            todo.push(Trip{x, y - 1, z});
        }
        if(z > 0 && !visited[x][y][z - 1] && !grid[x][y][z - 1]){
            visited[x][y][z - 1] = 1;
            todo.push(Trip{x, y, z - 1});
        }
        
    }

    //add unvisited dudes to grid
    for(int x = 0; x < 201; x ++){
        for(int y = 0; y < 201; y ++){
            for(int z = 0; z < 201; z ++){
                if(!visited[x][y][z]) grid[x][y][z] = 1;
            }
        }
    }





    int total = 0;
    for(int x = 0; x < 201; x ++){
        for(int y = 0; y < 201; y ++){
            for(int z = 0; z < 201; z ++){
                if(!grid[x][y][z])continue;
                if(!grid[x - 1][y][z]) total++;
                if(!grid[x + 1][y][z]) total++;
                if(!grid[x][y - 1][z]) total++;
                if(!grid[x][y + 1][z]) total++;
                if(!grid[x][y][z - 1]) total++;
                if(!grid[x][y][z + 1]) total++;
            }
        }
    }

    cout << total << endl;
    
}
