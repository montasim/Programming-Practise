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

    void ChangeProperties(){

        name = "Modefied";
        price = 100;
    }
};

int main(){
    Book book;
    book.ChangeProperties();
    cout << book.name << endl;
    cout << book.price << endl;

    Book newBook;
    cout << newBook.name << endl;
    cout << newBook.price << endl;
    return 0;
}
