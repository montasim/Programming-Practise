#include <stdio.h>
void printfunction(char* from_main)
{
    printf("%s\n", from_main);
}

int main()
{   
    printfunction("hello world");   
    return 0;
}