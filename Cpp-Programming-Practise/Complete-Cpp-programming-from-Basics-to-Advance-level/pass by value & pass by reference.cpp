#include <iostream>
#include <string.h>

using namespace std;

int changeValue(int* change){
    *change = 20;
}

int main()
{
    int number = 10;

    cout << number << endl;

    changeValue(&number);
    cout << number;

    return 0;
}



