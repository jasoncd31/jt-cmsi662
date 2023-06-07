//Stack in C

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

typedef struct Stack {
    Node *top;
} Stack;

Stack *createStack() {
    Stack *stack = (Stack *) malloc(sizeof(Stack));
    stack->top = NULL;
    return stack;
}

bool isEmpty(Stack *stack) {
    return stack->top == NULL;
}

void push(Stack *stack, int data) {
    Node *node = (Node *) malloc(sizeof(Node));
    node->data = data;
    node->next = stack->top;
    stack->top = node;
}

int pop(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty\n");
        return -1;
    }
    Node *node = stack->top;
    int data = node->data;
    stack->top = node->next;
    free(node);
    return data;
}

int peek(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty\n");
        return -1;
    }
    return stack->top->data;
}

void printStack(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty\n");
        return;
    }
    Node *node = stack->top;
    while (node != NULL) {
        printf("%d ", node->data);
        node = node->next;
    }
    printf("\n");
}

int main() {
    Stack *stack = createStack();
    push(stack, 1);
    push(stack, 2);
    push(stack, 3);
    printStack(stack);
    printf("%d\n", pop(stack));
    printf("%d\n", peek(stack));
    printStack(stack);
    return 0;
}