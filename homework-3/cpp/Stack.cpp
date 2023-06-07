#include <iostream>
#include <memory>
#include <string>

namespace Validate {
void ok(bool condition, const std::string& message) {
    if (!condition) {
        throw std::invalid_argument(message);
    }
}

void notNull(const void* value) {
    ok(value != nullptr, "String must not be null");
}

void notEmpty(int topIndex) {
    ok(topIndex != 0, "Stack is empty");
}

void integerRange(int value, int minimum, int maximum) {
    ok(value >= minimum, "Must be at least " + std::to_string(minimum));
    ok(value <= maximum, "Must be at most " + std::to_string(maximum));
}
}  // namespace Validate
using namespace std;

template <typename T>

class Stack {
   private:
    unique_ptr<T[]> data;
    int size;
    int capacity;

   public:
    Stack() {
        data = make_unique<T[]>(1);
        size = 0;
        capacity = 1;
    }

    ~Stack() = default;

    void push(T value) {
        Validate::notNull(&value);
        if (size == capacity) {
            auto new_data = make_unique<T[]>(capacity * 2);
            for (int i = 0; i < size; i++) {
                new_data[i] = data[i];
            }
            data = std::move(new_data);
            capacity *= 2;
        }
        data[size++] = value;
    }

    T pop() {
        Validate::notEmpty(topIndex);
        T value = data[--size];
        return value;
    }

    T peek() {
        Validate::notEmpty(topIndex);
        return data[size - 1];
    }

    bool empty() const {
        return size == 0;
    }

    int getSize() const {
        return size;
    }
};

int main() {
    Stack<std::string> stack;
    stack.push("Hello");
    stack.push("World");
    std::cout << "Size: " << stack.getSize() << std::endl;
    std::cout << "Top element: " << stack.peek() << std::endl;
    std::cout << "Popped element: " << stack.pop() << std::endl;
    std::cout << "Size: " << stack.getSize() << std::endl;

    return 0;
}
