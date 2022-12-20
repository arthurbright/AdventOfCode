#include <bits/stdc++.h>
#include <iostream>
using namespace std;

ifstream f{"input"};

const int SIZE = 5000;
struct Num{
    long long v;
    int b;
};

Num nums[5000];
const long long OOGA = 811589153;

int main()
{
    long long inp;
    for(int i = 0; i < SIZE; i ++){
        f >> inp;
        nums[i] = Num{OOGA * inp, i};
    }

    //scrable
    for(int time = 0; time < 10; time ++){

    
        for(int i = 0; i < SIZE; i ++){
            //find the first unmoved boi
            int cur = -69;
            for(int j = 0; j < SIZE; j ++){
                if(nums[j].b == i){
                    cur = j;
                    break;
                }
            }

            //move cur
            long long val = nums[cur].v;
            long long vall = val % (SIZE - 1);
            if(val < 0){
                for(int off = -1; off >= vall; off--){
                    swap(nums[(cur + off + 3 * SIZE) % SIZE], nums[(cur + off + 3 * SIZE + 1) % SIZE]);
                }
            }
            else if(val > 0){
                for(int off = 1; off <= vall; off++){
                    swap(nums[(cur + off + SIZE) % SIZE], nums[(cur + off + SIZE - 1) % SIZE]);
                }
            }

        }/*
         for(int i = 0; i < SIZE; i ++){
                    cout << nums[i].v <<", ";
                }
            cout << endl;*/
    }

    int Z = -1;
    for(int i = 0; i < SIZE; i ++){
        if(nums[i].v == 0){
            Z = i;
            break;
        }
    }


    //cerr << "gither";
    cout << (nums[(Z + 1000) % SIZE].v + nums[(Z + 2000) % SIZE].v + nums[(Z + 3000) % SIZE].v) << endl;
    
}
