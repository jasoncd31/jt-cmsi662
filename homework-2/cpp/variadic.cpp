// Code partially generated using OpenAI's ChatGPT
// This solution goes the recursive route to calculate the sum of a variadic number of arguments
#include <iostream>

// Base case: when there are no more arguments, return 0
int sum() {
    return 0;
}

// Recursive case: calculate the sum of the first argument and the sum of the remaining arguments
template<typename T, typename... Args>
int sum(T value, Args... args) {
    return value + sum(args...);
}

int main() {
    int result = sum(1, 2, 3, 4, 5);
    std::cout << "Sum: " << result << std::endl;
    return 0;
}