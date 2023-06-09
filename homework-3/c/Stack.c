//Stack in C

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "stack.h"

#define STACK_UNDERFLOW -1
#define STACK_OVERFLOW -2
#define NULL_POINTER -3
#define MAX_CAPACITY 2048 

struct stack {
    char** elements;
    unsigned int top;
    unsigned int capacity;
};

Stack *stack_create(unsigned int capacity) {
    Stack stack = (Stack) malloc(sizeof(Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->elements = (char**) malloc(stack->capacity * sizeof(char*));
    return stack;
}

bool stack_is_empty(const Stack stack) {
    return stack->top == -1;
}

bool stack_is_full(Stack stack) {
    return stack->top == stack->capacity - 1;
}

void stack_push(Stack stack, char* item) {
    if (strlen(item) > MAX_CAPACITY) {
        exit(STACK_OVERFLOW);
    }
    if (item == NULL) {
        exit(NULL_POINTER);
    }
    if (stack_is_full(stack)) {
        stack->elements = realloc(stack->elements, stack->capacity * 2);
        stack->capacity *= 2;
    }
    stack->elements[++stack->top] = item;
}

char* stack_pop(Stack stack) {
    //you can null out the memory
    if (stack_is_empty(stack)) {
        exit(STACK_UNDERFLOW);
    }
    else if (stack->top < stack->capacity / 2) {
        stack->elements = realloc(stack->elements, stack->capacity / 2);
        stack->capacity /= 2;
    }
    char* item = stack->elements[stack->top--];
    stack->elements[stack->top + 1] = NULL;
    return item;
}

char* stack_peek(Stack stack) {
    if (stack_is_empty(stack)) {
        exit(STACK_UNDERFLOW);
    }
    return stack->elements[stack->top];
}

void stack_destroy(Stack stack) {
    free(stack->elements);
    free(stack);
}

int main() {
    Stack *stack = stack_create(2);
    stack_push(stack, "Hello");
    stack_push(stack, "World");
    stack_push(stack, "!");
    stack_push(stack, "?");
    printf("%s\n", stack_pop(stack));
    printf("%s\n", stack_pop(stack));
    stack_destroy(stack);
    return 0;
}