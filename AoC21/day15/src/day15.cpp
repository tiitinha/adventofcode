#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <climits>
#include <cmath>

using namespace std;

struct Node {
    int value;
    int f;
    int x;
    int y;
    bool operator<(const Node &rhs) const {
        return f < rhs.f;
    }
};

struct compare {
   bool operator()(const Node& l, const Node& r) {
       return l.f > r.f;
   }
};

vector<vector<Node>> read_input() {
    string line;
    string val;
    ifstream myfile("../test.txt");
    vector<vector<Node>> nodes;
    int x, y = 0;

    if (myfile) {
        while (getline(myfile, line)) {
            vector<Node> node_row;
            for (char val : line) {
                Node new_node;
                new_node.f = (x == 0 && y == 0) ? 0 : INT_MAX;
                new_node.x = x;
                new_node.y = y;
                new_node.value = val - '0';
                node_row.push_back(new_node);
                x++;
            }
            y++;
            x = 0;
            nodes.push_back(node_row);
        }
    }

    return nodes;
}

bool isVisited(vector<vector<bool>> visited, int x, int y) {
    return visited[x][y];
}

bool isSafe(int xPosition, int yPosition, int rows, int columns) {
    return (xPosition >= 0 && xPosition < rows && yPosition >= 0 && yPosition < columns);
}

Node minDistVertex(vector<vector<Node>> nodes, Node current, vector<vector<bool>> visited) {
    int x = current.x;
    int y = current.y;
    Node minDistNode;
    int minDist = INT_MAX;
    int currentDist = current.f;

    for (int i = -1; i <= 1; i++) {
        for (int j = -1; j <= 1; j++) {
            if (isSafe((x + i), (y + j), nodes[0].size(), nodes.size()) && abs(i) != abs(j) && !(i == 0 && j == 0) && !isVisited(visited, (x + i), (y + j))) {
                cout << (x + i) << ", " << (y + j) << endl;
                int dist = currentDist + nodes[y + j][x + i].value;
                nodes[y + j][x + i].f = dist;

                if (dist < minDist) {
                    minDist = currentDist + nodes[y + j][x + i].value;
                    minDistNode = nodes[y + j][x + i];
                }
            }
        }
    }

    cout << "x: " << minDistNode.x << " y: " << minDistNode.y << ", F: " << minDistNode.f  << endl;

    return minDistNode;
}

priority_queue<Node, vector<Node>, compare> initQueue(vector<vector<Node>> nodes) {
    priority_queue<Node, vector<Node>, compare> q;
    q.push(nodes[0][0]);

    return q;
}

int dijkstra(vector<vector<Node>> nodes) {
    priority_queue<Node, vector<Node>, compare> q = initQueue(nodes);
    vector<vector<bool>> visited(nodes.size(), vector<bool>(nodes[0].size(), 0));
    Node next;
    Node minDist;
    int rows = nodes[0].size();
    int cols = nodes.size();

    while (!q.empty()) {
        next = q.top();
        q.pop();

        cout << "next: " << next.x << ", " << next.y << endl;

        if (isVisited(visited, next.x, next.y)) {
            cout << "visited" << endl;
            continue;
        }

        minDist = minDistVertex(nodes, next, visited);
        q.push(minDist);

        visited[next.x][next.y] = 1;

        if (next.x == rows - 1 && next.y == cols - 1) {
            cout << "breik" << endl;
            break;
        }

    }


    return nodes[rows -1][cols - 1].f;
}


int main() {
    vector<vector<Node>> nodes;
    int risk;

    nodes = read_input();
    risk = dijkstra(nodes);

    cout << risk << endl;
    return 0;
}
