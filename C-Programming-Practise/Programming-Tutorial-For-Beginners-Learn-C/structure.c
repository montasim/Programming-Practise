#include <stdio.h>
#include <string.h>

    
int main()
{   
    struct Books
    {
        char book_name[50];
        char author[50];
        int price;
    };

    struct Books bk1, bk2;
    strcpy(bk1.book_name, "learn c");
    strcpy(bk1.author, "montasim");
    bk1.price=100;

    printf("%s\n", bk1.book_name);
    printf("%s\n", bk1.author);
    printf("%d\n", bk1.price);
    return 0;
}