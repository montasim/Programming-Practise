#include <iostream>
#include <string.h>

using namespace std;

int main()
{
    int a=1, b=2, c=3;
    int *array[] = {&a, &b, &c};
    for(int i=0; i<3; i++){
        cout << *array[i] << endl;
    }
    return 0;
}



