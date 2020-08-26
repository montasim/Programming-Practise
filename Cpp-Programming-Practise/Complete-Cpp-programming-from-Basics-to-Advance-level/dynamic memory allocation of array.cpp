#include <iostream>
#include <string.h>

using namespace std;

int main()
{
    string *array;
    int number;
    cin >> number;

    array = new string[number];

    for(int i=0; i<number; i++){
        cin >> array[i];
    }


    for(int i=0; i<number; i++){
        cout << array[i] << endl;
    }
    return 0;
}




