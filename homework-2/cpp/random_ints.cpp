// code partially generated using Google's Bard

#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    // initialize random seed which prevents the issues of getting the same random numbers
    srand(time(0));

    int random_integer;

    for(int index = 0; index < 10; index++)
    {
        random_integer = (rand()%100)+1;
        cout << random_integer << endl;
    }
    return 0;
}