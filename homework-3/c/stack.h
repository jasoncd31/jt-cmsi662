//A header file for the Stack class in C

#ifndef STACK_H
#define STACK_H

#include <stdbool.h>

typedef struct stack* Stack;

Stack *stack_create(unsigned int capacity);
void stack_destroy(Stack s);
void stack_push(Stack s, char* value);
char *stack_pop(Stack s);
char *stack_peek(Stack s);
bool stack_is_empty(Stack s);
bool stack_is_full(Stack s);
int stack_getSize(Stack s);

#endif