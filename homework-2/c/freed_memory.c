// code partially generated using GitHub Copilot and Google's Bard
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char *return_val = 0;
    const size_t buffer_size = strlen(argv[0]) + 1;

    char *buffer= (char *)malloc(buffer_size);
    if (buffer== NULL)
    {
        fprintf(stderr, "malloc failed\n");
        return 1;
    }

    for (size_t i = 0; i < buffer_size; i++)
    {
        buffer[i] = argv[0][i];
    }

    free(buffer);
    return 0;
}
