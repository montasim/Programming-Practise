#include <iostream>
#include <string>
using namespace std;

class Book{
public:
    // properties/variables
    string name;
    float price;

    // functions
    Book(){
        name = "Default";
        price = 00.00;
    }
};

int main(){
    Book book;
    cout << book.name << endl;
    cout << book.price << endl;
    return 0;
}
