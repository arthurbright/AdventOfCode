#include <bits/stdc++.h>
#include <iostream>
using namespace std;

ifstream f{"input"};
bool rock[10110][9];

vector<vector<bool>> pieces[5];

struct Piece{
    long long r;
    long long c;
    vector<vector<bool>> bits;
};

bool intersect(Piece &p){
    for(int r = 0; r < p.bits.size(); r ++){
        for(int c = 0; c < p.bits[0].size(); c++){
            if(p.bits[r][c] && rock[p.r + r][p.c + c]){
                return true;
            }
        }
    }
    return false;
}

int main()
{
    long long height = 0;
    string input;
    f >> input;
    //setup
    for(int i = 0; i < 10110; i ++){
        rock[i][0] = 1;
        rock[i][8] = 1;
    }
    for(int i = 0; i < 9; i ++){
        rock[0][i] = 1;
    }

    pieces[0] = vector<vector<bool>>{vector<bool>{1, 1, 1, 1}};
    pieces[1] = vector<vector<bool>>{vector<bool>{0, 1, 0}, vector<bool>{1, 1, 1}, vector<bool>{0, 1, 0}};
    pieces[2] = vector<vector<bool>>{vector<bool>{1, 1, 1}, vector<bool>{0, 0, 1}, vector<bool>{0, 0, 1}};
    pieces[3] = vector<vector<bool>>{vector<bool>{1}, vector<bool>{1}, vector<bool>{1}, vector<bool>{1}};
    pieces[4] = vector<vector<bool>>{vector<bool>{1, 1}, vector<bool>{1, 1}};

    Piece piece;
    int count = 0;
    for(int i = 0; i <= 1729; i ++){
        //spawn location
        piece.r = height + 4;
        piece.c = 3;
        piece.bits = pieces[i % 5];

        //drop piece
        while(true){
            //gas
            if(input[count % 10091] == '>'){
                //attempt move right
                piece.c ++;
                if(intersect(piece)){
                    piece.c --;
                }
            }
            else{
                //attemp move left
                piece.c --;
                if(intersect(piece)){
                    piece.c ++;
                }
            }
            count ++;

            //attempt move down
            piece.r --;
            if(intersect(piece)){
                piece.r ++;
                //find new max height
                for(int r = 0; r < piece.bits.size(); r ++){
                    for(int c = 0; c < piece.bits[0].size(); c ++){
                        if(piece.bits[r][c]){
                            rock[piece.r + r][piece.c + c] = 1;
                            height = max(height, piece.r + r);
                        }
                    }
                }
                break;
            }
        }

        bool hi = true;
        for(int i = 1; i <= 7; i ++){
            if(!rock[height][i]){
                hi = false;
                break;
            }
        }

        if(hi) cout << "FLATEAU " << count % 10091 << ", " << i << ", " << height << endl;
    }

    for(int i = height + 1; i >= height -10; i --){
        for(int c = 0; c < 9; c ++){
            if(rock[i][c]) cout << "X";
            else cout << (i == height + 1? "-": ".");
        }
        cout << endl;
    }
    cout << count % 10091 << endl;
    cout << height << endl;
    //1e12
    
}
