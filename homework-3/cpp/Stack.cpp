//a c++ program that makes a Stack class using smart pointers

#include <iostream>
#include <memory>
#include <string>

using namespace std;

class Stack {
    private:
        unique_ptr<string[]> array;
        int top;
        int capacity;
    public:
        Stack(unsigned int capacity) {
            this->array = make_unique<string[]>(capacity);
            this->top = -1;
            this->capacity = capacity;
        }
        ~Stack() {
            cout << "Stack destructor called" << endl;
        }
        void push(string value) {
            if (this->isFull()) {
                cout << "Stack is full" << endl;
                return;
            }
            this->top++;
            this->array[this->top] = value;
        }
        string pop() {
            if (this->isEmpty()) {
                cout << "Stack is empty" << endl;
                return "";
            }
            string value = this->array[this->top];
            this->top--;
            return value;
        }
        string peek() {
            if (this->isEmpty()) {
                cout << "Stack is empty" << endl;
                return "";
            }
            return this->array[this->top];
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
};



int main(){
    //make a stack object
    Stack s(5);
    //push some values
    s.push("hello");
    s.push("world");
    s.push("this");
    s.push("is");
    s.push("a");
    s.push("test");
    //pop some values
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    //peek at the top value
    cout << s.peek() << endl;
    //get the size of the stack
    cout << s.getSize() << endl;
    return 0;
}