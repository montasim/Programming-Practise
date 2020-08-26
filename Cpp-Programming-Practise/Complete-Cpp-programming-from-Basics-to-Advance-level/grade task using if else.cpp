#include <iostream>

using namespace std;

int main()
{
    int number;

    cout << "Enter a number: ";
    cin >> number;

    if(number <= 100 && number >= 80){
        cout << "Grade is A" << endl;
    }
    if(number <= 79 && number >= 70){
        cout << "Grade is B" << endl;
    }
    if(number <= 69 && number >= 60){
        cout << "Grade is C" << endl;
    }
    if(number <= 59 && number >= 50){
        cout << "Grade is C" << endl;
    }
    if(number < 50){
        cout << "Grade is FAIL" << endl;
    }
    else{
        cout << "Wrong input";
    }

    return 0;
}

