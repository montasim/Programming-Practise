#include <iostream>

using namespace std;

int main()
{
    int a = 4,
        b = 7,
        c = 60;

    if(a < b && a < c){
        cout << "a is less than b and c" << endl;
    }
    else{
        cout << "b is less than a" << endl;
    }

    return 0;
}

