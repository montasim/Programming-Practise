#include <iostream>

using namespace std;

int main()
{
    int num;
    cout << "Enter your number: ";
    cin >> num;

    int temp = 1;

    while(temp != 11){
        cout << num << " * " << temp << " = " << num * temp << endl;
        temp++;
    }

    return 0;
}

