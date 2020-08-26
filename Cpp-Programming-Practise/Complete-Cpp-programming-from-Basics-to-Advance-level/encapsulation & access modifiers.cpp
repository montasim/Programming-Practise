#include <iostream>
#include <string.h>

using namespace std;

class Book{
private:
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

int main()
{

    Book book("c", "condition", "me", 200);
    //book2.setPrice();
    cout << book.name << endl;

    book.setAuthor("montasim");
    book.author = "mamun";

    cout << book.author;

    return 0;
}


