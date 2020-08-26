#include <iostream>

using namespace std;

int main()
{
    int input;
    int factorial = 1;
    cout << "Enter your number for calculate factorial: ";
    cin >> input;
    for(int i=1; i <= input; i++){

        factorial = factorial * i;
    }

    cout << "Factorial of "<< input << " is " << factorial << endl;

    return 0;
}

