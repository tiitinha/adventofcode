#ifndef DIJKSTRA_H
#define DIJKSTRA_H

#include <vector>

using namespace std;

struct Dijkstra {
    int arc_value;
    std::vector<Dijkstra> unvisited;
    std::vector<Dijkstra> visited;
    int arcsum;
    int algo();
};

#endif
