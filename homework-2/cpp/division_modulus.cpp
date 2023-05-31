#include <iostream>
#include <vector>
#include <limits>

using namespace std;

vector<int> greedyChangeMaker(int amount, const vector<int>& denominations) {
    vector<int> result;
    
    for (int i = 0; i < denominations.size(); i++) {
        int denomination = denominations[i];
        if (denomination <= 0 || ((amount == numeric_limits<int>::min() && denomination == -1))) {
          throw runtime_error("Invalid for division");
        }
        result.push_back(amount / denomination);
        amount = amount % denomination;
    }
    
    return result;
}

void printCoins(int amount, vector<int>& denominations, vector<int>& change) {
  cout << "Change for " << amount << ": ";
    for (int i = 0; i < denominations.size(); i++) {
      cout << denominations[i] << " cent(s): " << change[i] << ", ";
    }
    cout << endl;
}

int main() {
  try {
    int amount = 63;
    vector<int> denominations = {25, 10, 5, 1};
    vector<int> change = greedyChangeMaker(amount, denominations);
  printCoins(amount, denominations, change);
  } catch(const exception& ex) {
    cerr << "Exception caught: " << ex.what() << std::endl;
  }

  try {
    int amount = 63;
    vector<int> denominations = {25, 10, -5, 1};
    vector<int> change = greedyChangeMaker(amount, denominations);
  printCoins(amount, denominations, change);
  } catch(const exception& ex) {
    cerr << "Exception caught: " << ex.what() << std::endl;
  }

  try {
    int amount = 63;
    vector<int> denominations = {25, 10, 5, 0};
    vector<int> change = greedyChangeMaker(amount, denominations);
  printCoins(amount, denominations, change);
  } catch(const exception& ex) {
    cerr << "Exception caught: " << ex.what() << std::endl;
  }
    
    return 0;
}