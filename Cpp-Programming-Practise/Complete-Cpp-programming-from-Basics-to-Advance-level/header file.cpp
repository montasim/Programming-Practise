#include <iostream>
#include <string.h>

using namespace std;

int main()
{
    string name;
    int a, b;

    cout << "Enter your name: " << endl;
    cin >> name;

    cout << "Enter value of a: " << endl;
    cin >> a;

    cout << "Enter value of b: " << endl;
    cin >> b;

    cout << "Your name is:" << name << endl;
    cout << "Sum of a and b is:" << a+b << endl;

    return 0;
}

