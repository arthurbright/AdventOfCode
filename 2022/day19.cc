#include <bits/stdc++.h>
#include <iostream>
using namespace std;

ifstream f{"input"};

struct State{
    size_t ore, clay, obsidian, geode;
    size_t oreBot, clayBot, obsidianBot;

    size_t operator()(const State& t) const noexcept{
        return t.ore + t.clay>>7 + t.obsidian>>14 + t.geode>>21 + t.oreBot>>28 + t.clayBot>>35 + t.obsidianBot>>42;
    }

    size_t hash() const noexcept{
        return ore | (clay<<7) | (obsidian<<14) | (geode<<21) | (oreBot<<28) |(clayBot<<35) | (obsidianBot<<42);
    }

};

bool operator==(const State &a, const State &b){
    return a.ore == b.ore && a.clay == b.clay && a.obsidian == b.obsidian && a.geode == b.geode && a.oreBot == b.oreBot && a.clayBot == b.clayBot && a.obsidianBot == b.obsidianBot;
}

int main()
{
    size_t total = 0;
    int b, oo, co, Oo, Oc, go, gO;
    for(int t = 0; t < 3; t ++){
        f >> b >> oo >> co >> Oo >> Oc >> go >> gO;
        
        queue<State> q;
        q.push(State{0, 0, 0, 0, 1, 0, 0});
        for(int i = 0; i < 31; i ++){
            size_t s = q.size();
            cout << "Starting round " << i << ", " << s << endl;
            unordered_set<size_t> checked;
            int MAXorebots = max(max(go, Oo), max(oo, co));
            int MAXclaybots = Oc;
            int MAXobbybots = gO;

            for(size_t j = 0; j < s; j ++){
                State t = q.front();
                q.pop();

                //process the state
                int canbuilds = 0;

                //build ore bot
                if(t.oreBot < MAXorebots && t.ore >= oo){
                    canbuilds++;
                    State temp{t.ore + t.oreBot - oo, t.clay + t.clayBot, t.obsidian + t.obsidianBot, t.geode, t.oreBot + 1, t.clayBot, t.obsidianBot};
                    if(checked.find(temp.hash()) == checked.end()){
                        q.push(temp);
                        checked.insert(temp.hash());
                    }
                
                }
                //build clay bot
                if(t.clayBot < MAXclaybots && t.ore >= co){
                    canbuilds++;
                    State temp{t.ore + t.oreBot - co, t.clay + t.clayBot, t.obsidian + t.obsidianBot, t.geode, t.oreBot, t.clayBot + 1, t.obsidianBot};
                    if(checked.find(temp.hash()) == checked.end()){
                        q.push(temp);
                        checked.insert(temp.hash());
                    }
                }
                //build obby bot
                if(t.obsidianBot < MAXobbybots && t.ore >= Oo && t.clay >= Oc){
                    canbuilds++;
                    State temp{t.ore + t.oreBot - Oo, t.clay + t.clayBot - Oc, t.obsidian + t.obsidianBot, t.geode, t.oreBot, t.clayBot, t.obsidianBot + 1};
                    if(checked.find(temp.hash()) == checked.end()){
                        q.push(temp);
                        checked.insert(temp.hash());
                    }
                }
                //build geode bot
                if(t.ore >= go && t.obsidian >= gO){
                    canbuilds++;
                    State temp{t.ore + t.oreBot - go, t.clay + t.clayBot, t.obsidian + t.obsidianBot - gO, t.geode + (31 - i), t.oreBot, t.clayBot, t.obsidianBot};
                    if(checked.find(temp.hash()) == checked.end()){
                        q.push(temp);
                        checked.insert(temp.hash());
                    }
                }


                //do nothing
                if(canbuilds < 4){
                    State temp{t.ore + t.oreBot, t.clay + t.clayBot, t.obsidian + t.obsidianBot, t.geode, t.oreBot, t.clayBot, t.obsidianBot};
                    if(checked.find(temp.hash()) == checked.end()){
                        q.push(temp);
                        checked.insert(temp.hash());
                    }
                }
            }
        }

        int s = q.size();
        size_t maxx = 0;
        for(int i = 0; i < s; i ++){
            //one last round
            State state = q.front();
            q.pop();
            maxx = max(maxx, state.geode);
        }

        total = max(total, maxx);

        cout << maxx << endl;
    }

    cout << total << endl;
    
}
