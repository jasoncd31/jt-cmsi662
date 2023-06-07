//Stack in C

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "stack.h"

#define STACK_UNDERFLOW -1
#define STACK_OVERFLOW -2

Stack *stack_create(unsigned int capacity) {
    Stack *stack = (Stack *) malloc(sizeof(Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = (char**) malloc(stack->capacity * sizeof(char*));
    return stack;
}

bool stack_is_empty(Stack *stack) {
    return stack->top == -1;
}

bool stack_is_full(Stack *stack) {
    return stack->top == stack->capacity - 1;
}

void stack_push(Stack *stack, char* item) {
    if (stack_is_full(stack)) {
        exit(STACK_OVERFLOW);
    }
    stack->array[++stack->top] = item;
}

char* stack_pop(Stack *stack) {
    if (stack_is_empty(stack)) {
        exit(STACK_UNDERFLOW);
    }
    return stack->array[stack->top--];
}

char* stack_peek(Stack *stack) {
    if (stack_is_empty(stack)) {
        exit(STACK_UNDERFLOW);
    }
    return stack->array[stack->top];
}

void stack_destroy(Stack *stack) {
    free(stack->array);
    free(stack);
}

int main() {
    Stack *stack = stack_create(10);
    stack_push(stack, "Hello");
    stack_push(stack, "World");
    printf("%s\n", stack_pop(stack));
    printf("%s\n", stack_pop(stack));
    stack_destroy(stack);
    return 0;
}