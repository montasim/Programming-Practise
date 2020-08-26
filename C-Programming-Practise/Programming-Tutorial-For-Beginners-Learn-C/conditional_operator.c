#include <stdio.h>
int main()
{
    int age;
    printf("enter your age: \n");
    scanf("%d", &age);

    age>17?printf("you can drive"):printf("you can not drive"); //  also known as short hand if else
    
    return 0;
}
