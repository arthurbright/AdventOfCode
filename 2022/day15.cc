#include <bits/stdc++.h>
#include <iostream>
using namespace std;

ifstream f{"input"};

vector<pair<int, int>> beacons;
vector<pair<int, int>> sensors;

int main()
{

    char ch;
    int r, c, r2, c2;
    for(int i = 0; i < 24; i ++){
        f >> c;
        f >> r;
        f >> c2;
        f >> r2;

        beacons.push_back({r2, c2});
        sensors.push_back({r, c});
        
    }


        
    for(int ii = 0; ii < 24; ii ++){
        int r = sensors[ii].first;
        int c = sensors[ii].second;
        int r2 = beacons[ii].first;
        int c2 = beacons[ii].second;
       
        int dist = abs(r - r2) + abs(c - c2) + 1;
        bool cant = false;

        //check perimietr
        for(int i = 0; i <= dist; i ++){
            int checkr = r - i;
            int checkc = c + (dist - i); //CHANGE

            if(checkr >= 0 && checkr <= 4000000 && checkc >= 0 && checkc <= 4000000){}
            else{
                continue;
            }
            cant = false;
            for(int s = 0; s < 24; s ++){
                int baddist = abs(sensors[s].first - beacons[s].first) + abs(sensors[s].second - beacons[s].second);
                
                if(abs(checkr - sensors[s].first) + abs(checkc - sensors[s].second) <= baddist){
                    cant = true;
                    break;
                }
            }

            if(cant) continue;
            cout << checkr << ", " << checkc << endl;
        }
    }


}
