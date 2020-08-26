#include <iostream>
using namespace std;

class Book
{
public:

    int price;

    Book()
    {
        price = 100;
    }
};

int main()
{
    Book book;
    cout << book.price;
}
