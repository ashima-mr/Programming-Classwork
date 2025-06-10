#include <iostream>
#include <vector> //dynamic arrays
#include <set> //only hold unique elements
#include <stack> //DFS

using namespace std; 

class EpsilonNFATransition {
public: 
    int state;
    char input;
    int NXTstate;
}; //dont forget semicolon

class EpsilonNFA {
public:
    int numStates;
    //vector of e transitions
    vector<set<int>> eTransitions; //vector of states with their set of e transition states
    //vector of all transitions
    vector<vector<EpsilonNFATransition>> transitions; //vector for a state, of vectors holding NFA transitions for all inputs
    
    //function to compute e closure of a state
    set<int> eClosure(int state) {
        set<int> visited;
        stack<int> dfsStack;
        
        visited.insert(state);
        dfsStack.push(state);
        
        while (!dfsStack.empty()){
            int currentState = dfsStack.top();
            dfsStack.pop();
            
            for (int nextState : eTransitions[currentState]) {
                if (visited.find(nextState) == visited.end()) { //if nextState is not in visited
                    visited.insert(nextState);
                    dfsStack.push(nextState);
                }
            }
        }
        return visited;
    }
    
    //function to compute e closure of all states
    vector<set<int>> computeEpsilonClosures() {
        vector<set<int>> epsilonClosures;

        for (int i = 0; i < numStates; ++i) { 
            epsilonClosures.push_back(eClosure(i));
        }

        return epsilonClosures;
    }
};

int main() {
     EpsilonNFA eNFA;
    cout << "21BAI1830\n";
    cout << "Enter the number of states: ";
    cin >> eNFA.numStates;

    cout << "Enter the transitions for each state (enter -1 to finish):\n";
    for (int i = 0; i < eNFA.numStates; ++i) {
        set<int> transitionsSet;
        int transition;
        cout << "Transitions for State " << i << ": ";
        while (cin >> transition && transition != -1) {
            transitionsSet.insert(transition);
        }
        eNFA.eTransitions.push_back(transitionsSet);
    }

    vector<set<int>> epsilonClosures = eNFA.computeEpsilonClosures();

    for (int i = 0; i < eNFA.numStates; ++i) {
        cout << "Epsilon Closure of State " << i << ": ";
        for (int state : epsilonClosures[i]) {
            cout << state << " ";
        }
        cout << endl;
    }

    return 0;
}