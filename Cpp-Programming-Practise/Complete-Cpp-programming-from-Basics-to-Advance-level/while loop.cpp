#include <iostream>

using namespace std;

int main()
{
    int counter;

    cout << "How many times you want the loop to run: ";
    cin >> counter;

    while(counter > 0){

     cout << "loop" << endl;
        counter--;
    }

    return 0;
}

