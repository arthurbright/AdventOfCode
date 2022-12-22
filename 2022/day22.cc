#include <bits/stdc++.h>
#include <iostream>
using namespace std;

ifstream f{"input"};

int grid[202][152];

int vr = 0;
int vc = 1;
int r = 1;
int c = 51;
int gr;
int gc;

                /*faces
 12
 3
45
6 
*/

void addFace(int face){
    if(face == 1){
        gc += 50;
    }
    else if(face == 2){
        gc += 100;
    }
    else if(face == 3){
        gr += 50;
        gc += 50;
    }
    else if(face == 4){
        gr += 100;
    }
    else if(face == 5){
        gr += 100;
        gc += 50;
    }
    else if(face == 6){
        gr += 150;
    }
    else{
        cerr << face << endl;
        throw 0;
    }
}

void clock(int face){
    //cout << r << " |||| " << c << endl;
    gr --;
    gc --;
    int tempr = gr;
    int tempc = gc;
    tempr = gc;
    tempc = 49 - gr;
    gr = (tempr + 500) % 50 + 1;
    gc = (tempc + 500) % 50 + 1;
    //cout << gr << " |||| " << gc << endl;
    addFace(face);
}

void cclock(int face){
    gr --;
    gc --;
    int tempr = gr;
    int tempc = gc;
    tempr = 49 - gc;
    tempc = gr;
    gr = (tempr + 500) % 50 + 1;
    gc = (tempc + 500) % 50 + 1;
    addFace(face);
}


int face(){
    if(r <= 50){
        if(c <= 100){
            return 1;
        }
        return 2;
    }

    if(r <= 100) return 3;
    if(r <= 150){
        if(c <= 50) return 4;
        return 5;
    }
    return 6;
}

void left(){
    int newc = vr;
    int newr = 0 - vc;
    vr = newr;
    vc = newc;
}

void right(){
    int newc = 0 - vr;
    int newr = vc;
    vr = newr;
    vc = newc;
}

int main()
{
    string str;
    for(int i = 1; i <= 200; i ++){
        getline(f, str);
        for(int j = 0; j < str.size(); j ++){
            if(str[j] == '.') grid[i][j + 1] = 1;
            else if(str[j] == '#') grid[i][j + 1] = 2;
        }
    }

    getline(f, str);


    int n;
    char dir;
    while(f >> n){
        //move
        //cerr << r << ", " << c << ", " << vr << ", " << vc << " || " << n << endl;
        for(int i = 0; i < n; i ++){
            if(grid[r + vr][c + vc] == 1){
                //move
                r += vr;
                c += vc;
            }
            else if(grid[r + vr][c + vc] == 2){
                break;
            }
            else{
                /*faces
                
 12
 3
45
6 
*/
                //calculate goal pos
                gr = r + vr;
                gc = c + vc;
                if(face() == 1){
                    if(vr == -1){
                        clock(6);
                        if(grid[gr][gc] == 1){
                            r = gr;
                            c = gc;
                           right();
                        }
                    }
                    else if(vc == -1){
                        clock(4);
                        //cout << gr << " |||| " << gc << endl;
                        clock(4);
                                                cout << gr << " |||| " << gc << endl;
                        if(grid[gr][gc] == 1){
                            r = gr;
                            c = gc;
                            left();
                            left();
                        }
                    }
                }
                else if(face() == 2){
                    if(vr == -1){
                        clock(6);
                        cclock(6);
                        if(grid[gr][gc] == 1){
                            r = gr;
                            c = gc;
                        }
                    }
                    else if(vc == 1){
                        clock(5);
                        clock(5);
                        if(grid[gr][gc] == 1){
                            r = gr;
                            c = gc;
                            left();
                            left();
                        }
                    }
                    else if(vr == 1){
                        clock(3);
                        if(grid[gr][gc] == 1){
                            r = gr;
                            c = gc;
                            right();
                        }
                    }
                }
                else if(face() == 3){
                    if(vc == 1){
                        cclock(2);
                        if(grid[gr][gc] == 1){
                            r = gr;
                            c = gc;
                            left();
                        }
                    }
                    else if(vc == -1){
                        cclock(4);
                        if(grid[gr][gc] == 1){
                            r = gr;
                            c = gc;
                            left();
                        }
                    }
                }
                else if(face() == 4){
                    if(vc == -1){
                        clock(1);
                        clock(1);
                        if(grid[gr][gc] == 1){
                            r = gr;
                            c = gc;
                            right();
                            right();
                        }
                    }
                    else if(vr == -1){
                        clock(3);
                        if(grid[gr][gc] == 1){
                            r = gr;
                            c = gc;
                            right();
                        }
                    }
                }
                else if(face() == 5){
                    if(vc == 1){
                        clock(2);
                        clock(2);
                        if(grid[gr][gc] == 1){
                            r = gr;
                            c = gc;
                            left();
                            left();
                        }
                    }
                    else if(vr == 1){
                        clock(6);
                        if(grid[gr][gc] == 1){
                            r = gr;
                            c = gc;
                            right();
                        }
                    }
                }
                else if(face() == 6){
                    if(vc == -1){
                        cclock(1);
                        if(grid[gr][gc] == 1){
                            r = gr;
                            c = gc;
                            left();
                        }
                    }
                    else if(vr == 1){
                        cclock(2);
                        clock(2);
                        if(grid[gr][gc] == 1){
                            r = gr;
                            c = gc;
                        }
                    }
                    else if(vc == 1){
                        cclock(5);
                        if(grid[gr][gc] == 1){
                            r = gr;
                            c = gc;
                            left();
                        }
                    }
                }
                else throw "hi";

            }
        }

        //get direction
        if(! (f >> dir)) break;
        if(dir == 'L'){
            left();
        }
        else{
            right();
        }

    }

    cout << r  << ", " << c << ", " << vr << ", " << vc << endl;

}
