//c++ code that generates random integers

#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    srand(time(0));
    int random_integer;
    for(int index = 0; index < 10; index++)
    {
        random_integer = (rand()%100)+1;
        cout << random_integer << endl;
    }
    return 0;
}