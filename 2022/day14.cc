#include <bits/stdc++.h>
#include <iostream>
using namespace std;
bool wall[200][600];
bool sand[200][600];

ifstream f{"input"};

int main()
{
    int total = 0;
    int prevr, prevc;
    int r, c;
    char ch;
    int maxr = 0;
    for(int i = 0; i < 149; i ++){
        f >> c;
        c-= 200;
        f >> ch; //comma
        f >> r;
        maxr = max(maxr, r);
        while(true){
            f >> ch;
            if(ch == 'P') break;
            if(ch >= '0' && ch <= '9'){
                f.putback(ch);
                break;
            }
            prevr = r;
            prevc = c;
            //otherwise, read in the rest of arrow
            f >> ch;
            f >> c;
            c-= 200;
            f >> ch; //comma
            f >> r;
            maxr = max(maxr, r);

            //build wall
            for(int rr = min(prevr, r); rr <= max(r, prevr); rr++){
                for(int cc = min(prevc, c); cc <= max(c, prevc); cc++){
                    wall[rr][cc] = 1;
                }
            }

        }
    }

    maxr += 2;
    //build the max wall
    for(int i = 0; i < 600; i ++){
        wall[maxr][i] = 1;
    }

    //drop sand
    while(true){
        //spawn sand
        int sandr = 0;
        int sandc = 500 - 200;

        while(sandr < 200){
            if(!wall[sandr + 1][sandc]){
                sandr ++;
            }
            else if(!wall[sandr + 1][sandc - 1]){
                sandr ++;
                sandc --;
            }
            else if(!wall[sandr + 1][sandc + 1]){
                sandr ++;
                sandc ++;
            }
            else{
                //cannot move
                break;
            }
        }

        wall[sandr][sandc] = 1;
        sand[sandr][sandc] = 1;
        total += 1;
        if(sandr == 0 && sandc == 500 - 200){
            break;
        }
    }


    for(int i = 0; i < 200; i ++){
        for(int j = 0; j < 600; j ++){
            if(sand[i][j]) cout << "O";
            else if(wall[i][j]) cout << "#";
            else cout << ".";
        }
        cout << endl;
    }

    cout << total << endl;
}
