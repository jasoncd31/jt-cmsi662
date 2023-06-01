#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> numbers = {0, 1, 2, 3};
    int index = 3;

    // removes when in range
    if (index >= 0 && index < numbers.size()) {
      numbers.erase(numbers.begin() + index);
      cout << "remove successful \n";
    } else {
      cout << "remove unsuccessful \n";
    }

    // does nothing if index out of range
    if (index >= 0 && index < numbers.size()) {
      numbers.erase(numbers.begin() + index);
      cout << "remove successful \n";
    } else {
      cout << "remove unsuccessful \n";
    }
    
    return 0;
}