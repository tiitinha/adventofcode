#include <iostream>
#include <vector>

using namespace std;

class Module {
public:
    virtual int get_pulse() = 0;
    virtual string get_type() = 0;

    void set_pulse(int p) {
        pulse = p;
    }

    void add_to_previous(Module module) {
        previous.push(module);
    }
        
        
protected:
    string type;
    int pulse;
    vector<Module> previous;
};

class FlipFlop: public Module {
public:
    int getPulse() {
        return pulse;
    }

    int getState() {
        return state;
    }

    void setState(int s) {
        state = s;
    }
private:
    int state;
};

class Conjunction: public Module {
    
};


int main() {
    return 0;
}
