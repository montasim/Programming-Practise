#include <iostream>
#include <string.h>

using namespace std;

class Book{
protected:
    // Variables
    string name;
    string author;
    string title;
    int price;
    // function
    Book(){
        name = "";
        author = "";
        title = "";
        price = 00.00;
        cout << "constructor of book" << endl;
    }
    Book(string nameOfBook, string authorName, string titleOfBook, int priceOfBook){
        name = nameOfBook;
        author = authorName;
        title = titleOfBook;
        price = priceOfBook;
    }
    void setName(string nameValue){
        name = nameValue;
    }
    void setAuthor(string authorValue){
        author = authorValue;
    }
    void setTitle(string titleValue){
        title = titleValue;
    }
    void setPrice(int priceValue){
        price = priceValue;
    }

};

class Cookbook: public Book{
public:
    Cookbook(){
        cout << "Constructor of cookbook" << endl;
    }
    void recepie(){
        cout << "reciepe function";
    }

};

int main()
{
    Book book;
    Cookbook cookbook;
    cookbook.recepie();


    return 0;
}


