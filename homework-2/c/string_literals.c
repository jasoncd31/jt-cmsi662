// code partially generated using GitHub Copilot
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    // char *str = "Hi Dr. toal!";
    // The above line breaks the rule as its attempting to modify a string literal
    char str[] = "Hi Dr. toal!";
    str[7] = 'T';   
    return 0;
}