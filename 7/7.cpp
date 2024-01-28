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

vector<pair<vector<int>, int>> setup(bool useTxt, const string& testInput) {
    string line;
    vector<pair<vector<int>, int>> result;

    if (useTxt) {
        ifstream inputFile("input.txt");
        if (!inputFile) {
            cout << "Fant ikke filen\n";
            return result;
        }

        while (getline(inputFile, line)) {
            stringstream ss(line);
            string chars;
            int number;
            ss >> chars >> number;

            vector<int> intVec;
            for (char c : chars) {
                intVec.push_back(charToInt(c));
            }
            result.push_back(make_pair(intVec, number));
        }

        inputFile.close();
    } else {
        stringstream ss(testInput);
        while (getline(ss, line)) {
            stringstream lineStream(line);
            string chars;
            int number;
            lineStream >> chars >> number;

            vector<int> intVec;
            for (char c : chars) {
                intVec.push_back(charToInt(c));
            }
            result.push_back(make_pair(intVec, number));
        }
    }

    return result;
}

int handScore(const vector<int> hand, int wildCard) {
    map<int, int> cards;
    
    // Get the amount of each card 
    for (int card : hand) {
        if (card == 1) card = wildCard;
        if (cards.find(card) != cards.end() )
            cards[card] += 1;
        else 
            cards[card] = 1;
    }

    bool threeOfAKind = false;
    bool pair = false;
    for (const auto& card : cards) {
        switch (card.second) {
            case 5: return 7; break;
            case 4: return 6; break;
            case 3: 
                if (pair)           return 5;
                threeOfAKind = true;  
                break;
            case 2:
                if (threeOfAKind)   return 5;
                if (pair)           return 3;
                pair = true;
                break;
        }
    }

    if (threeOfAKind) return 4;
    else if (pair) return 2;

    return 1;
}

int maxCardScore(const vector<int> hand) {
    int maxScore = 0;
    for (int i = 2; i <= 14; i++) {
        int score = handScore(hand, i);
        if (score > maxScore) maxScore = score;
    }
    return maxScore; 
}

bool compareHands(const pair<vector<int>, int> handAo, const pair<vector<int>, int> handBo) {
    // return if handA has lower score than handB
    vector<int> handA = handAo.first, handB = handBo.first;

    int scoreA = maxCardScore(handA), scoreB = maxCardScore(handB);

    if (scoreA != scoreB) return scoreA < scoreB;

    for (int i = 0; i < handA.size(); i++)
        if (handA[i] != handB[i]) return handA[i] < handB[i];

    return true;
}

int task1(vector<pair<vector<int>, int>> hands) {
    int sum = 0;
    vector<pair<vector<int>, int>> handsSorted(hands);
    sort(handsSorted.begin(), handsSorted.end(), compareHands);

    for (int i = 1; i <= handsSorted.size(); i++)
        sum += i*handsSorted[i-1].second;

    return sum;
}

int main()  {
    string gTestInput = "32T3K 765\nT55J5 684\nKK677 28\nKTJJT 220\nQQQJA 483\n";
	vector<pair<vector<int>, int>> hands = setup(true, gTestInput);

    cout << task1(hands) << "\n";
	return 0;
}