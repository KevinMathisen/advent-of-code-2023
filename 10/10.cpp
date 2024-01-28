#include <iostream>                  //  cout
#include <string>                    //  string
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <map>
using namespace std;

vector<pair<int, int>> gPath = {};
vector<int> gDis1 = {}, gDis2={};
vector<vector<string>> gMap;
pair<int, int> gStartingPos;
int gCount1 = 0, gCount2 = 0;

string charToDir(char c) {
    if (c == '|') return "NS";
    if (c == '-') return "EW";
    if (c == 'L') return "NE";
    if (c == 'J') return "NW";
    if (c == '7') return "SW";
	if (c == 'F') return "SE";
	if (c == '.') return "";
	if (c == 'S') return "X";
    return ""; 
}

vector<vector<string>> setup(bool useTxt, const string& testInput) {
    string line;
    vector<vector<string>> result;
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

	// Process the remaining lines
    while (getline(ss, line)) {
        stringstream lineStream(line);
		vector<string> lineString;
		// Code for getting char and converting to string using charToDir() for each line in input
		char c;
		while (lineStream >> c) {
			lineString.push_back(charToDir(c));
		}

        result.push_back(lineString);
    }

    return result;
}

pair<int, int> getStartingPos(const vector<vector<string>> map) {
    for (int y = 0; y < map.size(); y++)
        for (int x = 0; x < map[y].size(); x++) 
            if (map[y][x] == "X") 
                return make_pair(x, y);

    return make_pair(-1, -1);
}

pair<pair<int, int>, char> createPath(const pair<int, int> pos, const char dirFrom, bool first) {
    // Save the pipe we're at
    gPath.push_back(pos);
    if (first) {
        gDis1.push_back(++gCount1);
    } else {
        gDis2.push_back(++gCount2);
    }

    // Get the direction we're heading
    string pipe = gMap[pos.second][pos.first];
    // Find which of the letters are pointing back towards the previous
    int newDir;
    if (dirFrom == 'N' && pipe[1] == 'S' || dirFrom == 'S' && pipe[1] == 'N' || dirFrom == 'E' && pipe[1] == 'W' || dirFrom == 'W' && pipe[1] == 'E') {
        newDir = 0; 
    } else 
        newDir = 1;

    char dir = pipe[newDir];

    // Get the new coordinates
    int x = 0, y = 0;
    if (dir == 'N') {
        y = -1;
    } else if (dir == 'S') {
        y = 1;
    } else if (dir == 'W') {
        x = -1;
    } else {
        x = 1;
    }
    
    // Return the next coordinates, and where we came from
    return make_pair( make_pair(pos.first+x, pos.second+y), dir);
}

int task1() {
    int sum = 0;

    int x = 0, y = 1;
    char dirFrom = 'S'; 
    pair<pair<int, int>, char> nextPipe = make_pair( make_pair(gStartingPos.first+x, gStartingPos.second+y), dirFrom);

    do {
        nextPipe = createPath(make_pair(nextPipe.first.first, nextPipe.first.second), nextPipe.second, true);
    } while (nextPipe.first != gStartingPos);

    x = -1; y = 0;
    dirFrom = 'W'; 
    nextPipe = make_pair( make_pair(gStartingPos.first+x, gStartingPos.second+y), dirFrom);

    do {
        nextPipe = createPath(make_pair(nextPipe.first.first, nextPipe.first.second), nextPipe.second, false);
    } while (nextPipe.first != gStartingPos);

    /* print
    for (int i = 0; i < gPath.size(); i++) {
        cout << " | x:" << gPath[i].first << " y:" << gPath[i].second;
    }*/
    if (gDis1.size() != gDis2.size())
        return -1;

    int max = 0;
    for (int i = 0; i < gDis1.size(); i++) 
        if (min(gDis1[i], gDis2[gDis2.size()-1-i]) > max)
                max = min(gDis1[i], gDis2[gDis2.size()-1-i]);

    return max;
}

int main()  {
    //string gTestInput = ".....\n.S-7.\n.|.|.\n.L-J.\n.....\n";
    string gTestInput = "..F7.\n.FJ|.\nSJ.L7\n|F--J\nLJ...\n";
	gMap = setup(true, gTestInput);
    gStartingPos = getStartingPos(gMap);

    cout << task1() << "\n";
	return 0;
}