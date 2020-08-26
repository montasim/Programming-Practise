#include <iostream>
#include <string.h>

using namespace std;

int main()
{
    int *pointers;
    int value = 10;

    pointers = &value;

    cout << pointers << endl;
    return 0;
}


