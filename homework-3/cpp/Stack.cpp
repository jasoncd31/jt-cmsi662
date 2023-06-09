//a c++ program that makes a Stack class using smart pointers

#include <iostream>
#include <memory>
#include <string>
#include <stdexcept>

using namespace std;

class Stack {
    private:
        unique_ptr<string[]> elements;
        int top;
        int capacity;
    public:
        Stack(unsigned int capacity) {
            validateIntegerRange(capacity, 0, 10000000);
            this->elements = make_unique<string[]>(capacity);
            this->top = -1;
            this->capacity = capacity;
        }

        ~Stack() {
            cout << "Stack destructor called" << endl;
        }

        void push(string value) {
            this->top++;
            this->elements[this->top] = value;
            refactorCapacity();
        }

        string pop() {
            if (this->isEmpty()) {
                throw out_of_range("Stack is empty");
            }
            string value = this->elements[this->top];
            this->top--;
            refactorCapacity();
            return value;
        }

        string peek() {
            if (this->isEmpty()) {
                throw out_of_range("Stack is empty");
            }
            return this->elements[this->top];
        }

        bool isEmpty() {
            return this->top == -1;
        }

        bool isFull() {
            return this->top == this->capacity - 1;
        }

        int getSize() {
            return this->top + 1;
        }

    private:
        void refactorCapacity() {
            int size = top + 1;
            if ((size == 1 && capacity != 1) || top == -1 || (size < capacity && size > static_cast<int>(capacity / 4))) {
                return;
            }
            double factor = (size == capacity ? 2.0 : 0.5);
            int newCapacity = static_cast<int>(capacity * factor);
            unique_ptr<std::string[]> refactoredStack = std::make_unique<std::string[]>(newCapacity);
            for (size_t i = 0; i < top+1; i++) {
                refactoredStack[i] = move(elements[i]);
            }
            elements = move(refactoredStack);
            capacity = newCapacity;
        }

        void validateIntegerRange(int value, int minimum, int maximum) {
            if (value <= minimum || value >= maximum) {
                throw out_of_range("value is out of range");
            }
        }
};



int main(){
    //make a stack object
    Stack s(6);
    //push some values
    s.push("hello");
    s.push("world");
    s.push("this");
    s.push("is");
    s.push("a");
    s.push("test");
    s.push("!");
    //pop some values
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    //peek at the top value
    cout << s.peek() << endl;
    //get the size of the stack
    cout << s.getSize() << endl;
    return 0;
}