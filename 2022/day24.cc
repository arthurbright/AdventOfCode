#include <bits/stdc++.h>
#include <iostream>
using namespace std;

//NOTE: TRIPLED INPUT

ifstream f{"input"};

const int ROWS = 109;
const int COLS = 102;
int grid[ROWS][COLS];
int grid2[ROWS][COLS];
bool visit[ROWS][COLS];
bool visit2[ROWS][COLS];


int main()
{
    string str;
    for(int i = 0; i < ROWS; i ++){
        getline(f, str);
        for(int j = 0; j < COLS; j ++){
            if(str[j] == '#'){
                grid[i][j] = 16;
            }
            else if(str[j] == '.'){
                grid[i][j] = 0;
            }
            else if(str[j] == '^'){
                grid[i][j] = 1;
            }
            else if(str[j] == '>'){
                grid[i][j] = 2;
            }
            else if(str[j] == 'v'){
                grid[i][j] = 4;
            }
            else if(str[j] == '<'){
                grid[i][j] = 8;
            }
        }
    }

    //input done
    //# = 16, . = 0,  ^>v< = 1248 (bitset)
    //bfs
    int steps = 0;
    visit[0][1] = true;
    while(true){
        //update grid 2
        for(int i = 0; i < ROWS; i ++){
            grid2[i][0] = 16;
            grid2[i][COLS - 1] = 16;
        }
        for(int j = 0; j < COLS; j ++){
            grid2[0][j] = 16;
            grid2[ROWS - 1][j] = 16;
            grid2[36][j] = 16;
            grid2[72][j] = 16;
        }
        grid2[0][1] = 0;
        grid2[ROWS - 1][COLS - 2] = 0;
        grid2[36][COLS - 2] = 0;
        grid2[72][1] = 0;
        for(int i = 1; i < ROWS - 1; i ++){
            for(int j = 1; j < COLS - 1; j ++){
                //move all blizzards
                if(grid[i][j] & 1){
                    //move up
                    if(i == 1 || i == 37 || i == 73){
                        grid2[i + 34][j] |= 1;
                    }
                    else{
                        grid2[i - 1][j] |= 1;
                    }
                }

                if(grid[i][j] & 2){
                    //move right
                    if(j == COLS - 2){
                        grid2[i][1] |= 2;
                    }
                    else{
                        grid2[i][j + 1] |= 2;
                    }
                }

                if(grid[i][j] & 4){
                    //move down
                    if(i == 35 || i == 71 || i == 107){
                        grid2[i - 34][j] |= 4;
                    }
                    else{
                        grid2[i + 1][j] |= 4;
                    }
                }

                if(grid[i][j] & 8){
                    //move left
                    if(j == 1){
                        grid2[i][COLS - 2] |= 8;
                    }
                    else{
                        grid2[i][j - 1] |= 8;
                    }
                }
            }
        }

        steps ++;

        swap(grid, grid2);
        //clear grid2;
        for(int i = 0; i < ROWS; i ++){
            for(int j = 0; j < COLS; j ++){
                grid2[i][j] = 0;
                //if(grid[i][j] == 16) cout << "#";
                //else cout << grid[i][j];
            }
            //cout << endl;
        }
        //cout << "=========================" << endl;

        //do a bfs on visit
        for(int i = 0; i < ROWS; i ++){
            for(int j = 0; j < COLS; j ++){
                if(visit[i][j]){
                    //wait
                    if(grid[i][j] == 0){
                        visit2[i][j] = true;
                    }
                    if(i + 1 < ROWS && grid[i + 1][j] == 0){
                        visit2[i + 1][j] = true;
                        if(i + 1 == ROWS - 1){
                            cout << steps << endl;
                            return 0;
                        }
                    }
                    if(i - 1 >= 0 && grid[i - 1][j] == 0){
                        visit2[i - 1][j] = true;
                    }
                    if(j + 1 < COLS && grid[i][j + 1] == 0){
                        visit2[i][j + 1] = true;
                    }
                    if(j - 1 >= 0 && grid[i][j - 1] == 0){
                        visit2[i][j - 1] = true;
                    }
                }
            }
        }

        swap(visit, visit2);
        //reset visit2
        for(int i = 0; i < ROWS; i ++){
            for(int j = 0; j < COLS; j ++){
                visit2[i][j] = 0;
            }
        }
        

    }


}   
    
