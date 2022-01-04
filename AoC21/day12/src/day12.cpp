#include <string>
#include <map>
#include "Strsplit.h"
#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

map<string, vector<string>> add_vertex(map<string, vector<string>> graph, string start, string end) {
    if (graph.count(start) == 0) {
        vector<string> edges;
        edges.push_back(end);
        graph.insert(pair<string, vector<string>> (start, edges));
    } else {
        vector<string> edges = graph[start];
        edges.push_back(end);
        graph.find(start)->second = edges;
    }

    return graph;
}

map<string, vector<string>> read_input() {
    string line;
    map<string, vector<string>> graph;
    ifstream myfile("../test.txt");
    string start;
    string end;

    if (myfile) {
        while (getline(myfile, line)) {
            vector<string> splitted = split(line, "-");
            vector<string> edges;

            start = splitted[0];
            end = splitted[1];

            graph = add_vertex(graph, start, end);
            if (end != "end" && start != "start") {
                graph = add_vertex(graph, end, start);
            }
        }
    }

    return graph;
}

int bfs(map<string, vector<string>> graph) {
    queue<string> q;
    string next;
    vector<string> edges;
    int count = 0;

    q.push("start");

    while (!q.empty()) {
        next = q.front();
        q.pop();

        edges = graph[next];

        for (string neighbor : edges) {
            q.push(neighbor);
            if (neighbor == "end") {
                count++;
                return count;
            }
        }
    }

    return count;
}

int main () {
    map<string, vector<string>> graph = read_input();
    int part1 = bfs(graph);

    cout << part1 << endl;

    return 0;
}
