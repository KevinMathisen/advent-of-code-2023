#include <iostream>                  //  cout
#include <string>                    //  string
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <map>
using namespace std;

vector<vector<vector<int>>> gReadings;

vector<vector<vector<int>>> setup(bool useTxt) {
    string testInput = "0 3 6 9 12 15\n1 3 6 10 15 21\n10 13 16 21 30 45\n";
    string line;
    vector<vector<vector<int>>> result;
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
        int value;
		vector<int> lineValues;

        while (lineStream >> value) {
            lineValues.push_back(value);
        }

        result.push_back({lineValues});
    }

    return result;
}
bool allZero(vector<int> values) {
    for (const auto& value : values) 
        if (value != 0) return false;
    return true;
}

void createPredictions(int readNum) {
    int currentSequence = 0;
    while (!allZero(gReadings[readNum][currentSequence])) {
        vector<int> nextSequence;
        for (int i = 1; i < gReadings[readNum][currentSequence].size(); i++)
            nextSequence.push_back(gReadings[readNum][currentSequence][i]-gReadings[readNum][currentSequence][i-1]);

        gReadings[readNum].push_back(nextSequence);
        currentSequence++;
    }
}

int task1() {
    int sum = 0;

    for (int i = 0; i < gReadings.size(); i++)
        createPredictions(i);

    // Calculate next values    
    for (int i = 0; i < gReadings.size(); i++) {
        int readingSize = gReadings[i].size()-1;
        gReadings[i][readingSize].push_back(0);
        for (int j = gReadings[i].size()-2; j >= 0; j--) {
            // Task 1
            //int newValue = gReadings[i][j][gReadings[i][j].size()-1] + gReadings[i][j+1][gReadings[i][j+1].size()-1];
            // Task 2 
            int newValue = gReadings[i][j][0] - gReadings[i][j+1][gReadings[i][j+1].size()-1];
            gReadings[i][j].push_back(newValue);
        }
    }
    // Calculate previous values 
    
    for (int i = 0; i < gReadings.size(); i++)
        sum += gReadings[i][0][gReadings[i][0].size()-1];

    return sum;
}



int main()  {
    gReadings = setup(true);
    cout << "Task 1: " << task1() << "\n";
	return 0;
}