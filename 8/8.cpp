#include <iostream>                  //  cout
#include <string>                    //  string
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <map>
using namespace std;

// Helper function to convert character to corresponding integer
int charToInt(char c) {
    if (c == 'T') return 10;
    if (c == 'J') return 1;
    if (c == 'Q') return 12;
    if (c == 'K') return 13;
    if (c == 'A') return 14;
    if (isdigit(c)) return c - '0';
    return -1; // Indicates an invalid character
}

pair<vector<char>, map<string, pair<string, string>>> setup(bool useTxt, const string& testInput) {
    string line;
    pair<vector<char>, map<string, pair<string, string>>> result;
    stringstream ss;

    if (useTxt) {
        ifstream inputFile("input.txt");
        if (!inputFile) {
            cout << "Fant ikke filen\n";
            return result;
        }
        ss << inputFile.rdbuf();
        inputFile.close();
    } else {
        ss = stringstream(testInput);
    }
	// Read first line into vector<char>
    if (getline(ss, line)) {
        for (char c : line) {
            result.first.push_back(c);
        }
    }

	// Process the remaining lines
    while (getline(ss, line)) {
        stringstream lineStream(line);
        string key, value1, value2;
        char equals, leftParen;

        // Parse the line according to the format: key = (value1,value2)
        if (!(lineStream >> key >> equals >> leftParen >> value1 >> value2)) {
            // Handle parsing error
            cout << "Error parsing line: " << line << endl;
            continue;
        }
        value1.erase(3, 1);
        value2.erase(3, 1);

        // Add to map
        result.second[key] = make_pair(value1, value2);
    }

    return result;
}


int task1(vector<char> directions, map<string, pair<string, string>> nodes) {
    int sum = 0;
    int currentDirStep = 0;

    pair<string, pair<string, string>> currentNode = make_pair("AAA", nodes["AAA"]);
    

    while (currentNode.first != "ZZZ") {
        string nextNode = (directions[currentDirStep++] == 'L') ? currentNode.second.first : currentNode.second.second;
        currentNode = make_pair(nextNode, nodes[nextNode]);
        if (currentDirStep % directions.size() == 0) currentDirStep = 0;
        sum++;
    }

    return sum;
}

/*
bool allNodesZ(vector<string> nodes) {
    for (const auto& node : nodes)
        if (node[2] != 'Z') return false;
    return true;
}

int task2(vector<char> directions, map<string, pair<string, string>> nodes) {
    int sum = 0;
    int currentDirStep = 0;

    vector<string> currentNodes;
    for (const auto& node : nodes) {
        if (node.first[2] == 'A') currentNodes.push_back(node.first);
    } 

    while (!allNodesZ(currentNodes)) {
        for (const auto& key: currentNodes) {
            string nextNode = (directions[currentDirStep] == 'L') ? nodes[key].first : nodes[key].second;
            auto it = find(currentNodes.begin(), currentNodes.end(), key);
            *it = nextNode;
        }
        
        if (++currentDirStep % directions.size() == 0) currentDirStep = 0;
        sum++;

        if (sum % 100000 == 0) cout << "\n step number " << sum;
    }

    return sum;
}*/

// Function to find the GCD of two numbers
long long gcd(long long a, long long b) {
    while (b != 0) {
        long long t = b;
        b = a % b;
        a = t;
    }
    return a;
}

long long task2(vector<char> directions, map<string, pair<string, string>> nodes) {

    vector<string> startNodes;
    vector<string> endNodes;
    vector<int> stepsToFinish, stepsToFinish2;
    for (const auto& node : nodes) {
        if (node.first[2] == 'A') startNodes.push_back(node.first);
    } 

    for (const auto& startNode : startNodes) {
        int sum = 0;
        int currentDirStep = 0;
        pair<string, pair<string, string>> currentNode = make_pair(startNode, nodes[startNode]);

        while (currentNode.first[2] != 'Z') {
            string nextNode = (directions[currentDirStep++] == 'L') ? currentNode.second.first : currentNode.second.second;
            currentNode = make_pair(nextNode, nodes[nextNode]);
            if (currentDirStep % directions.size() == 0) currentDirStep = 0;
            sum++;
        }
        endNodes.push_back(currentNode.first);

        stepsToFinish.push_back(sum);
    }

    for (const auto& startNode : endNodes) {
        int sum = 0;
        int currentDirStep = 0;
        pair<string, pair<string, string>> currentNode = make_pair(startNode, nodes[startNode]);

        do {
            string nextNode = (directions[currentDirStep++] == 'L') ? currentNode.second.first : currentNode.second.second;
            currentNode = make_pair(nextNode, nodes[nextNode]);
            if (currentDirStep % directions.size() == 0) currentDirStep = 0;
            sum++;
        } while (currentNode.first[2] != 'Z');

        stepsToFinish2.push_back(sum);
    }

    long long totalSum = static_cast<long long>(stepsToFinish[0]);
    for (int i = 1; i < stepsToFinish.size(); i++)
        totalSum = ( totalSum / gcd(totalSum, static_cast<long long>(stepsToFinish[i])) ) * static_cast<long long>(stepsToFinish[i]);

    return totalSum;
}

int main()  {
    //string gTestInput = "RL\n\nAAA = (BBB, CCC)\nBBB = (DDD, EEE)\nCCC = (ZZZ, GGG)\nDDD = (DDD, DDD)\nEEE = (EEE, EEE)\nGGG = (GGG, GGG)\nZZZ = (ZZZ, ZZZ)";
	//string gTestInput = "LLR\n\nAAA = (BBB, BBB)\nBBB = (AAA, ZZZ)\nZZZ = (ZZZ, ZZZ)\n";
    string gTestInput = "LR\n\n11A = (11B, XXX)\n11B = (XXX, 11Z)\n11Z = (11B, XXX)\n22A = (22B, XXX)\n22B = (22C, 22C)\n22C = (22Z, 22Z)\n22Z = (22B, 22B)\nXXX = (XXX, XXX)\n";
    pair<vector<char>, map<string, pair<string, string>>> input = setup(true, gTestInput);


    //cout << task1(input.first, input.second) << "\n";
    cout << task2(input.first, input.second) << "\n";
	return 0;
}