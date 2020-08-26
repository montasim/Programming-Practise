#include <iostream>
#include <string.h>

using namespace std;

int main()
{
    int *intPointer;
    int intValue = 10;

    float *floatPointer;
    float floatValue = 22.33;

    string *stringPointer;
    string stringValue = "hello";

    intPointer = &intValue;
    floatPointer = &floatValue;
    stringPointer = &stringValue;


    cout << intPointer << endl;
    cout << floatPointer << endl;
    cout << stringPointer << endl;
    return 0;
}


