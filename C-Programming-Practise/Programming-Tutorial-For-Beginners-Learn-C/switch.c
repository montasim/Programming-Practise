//  The switch statement allows us to execute one code block among many alternatives.
//  Else if statement is much better than switch statement
#include <stdio.h>
int main()
{
    int age;
    printf("enter your age: \n");
    scanf("%d", &age);

    switch (age)
    {
    case 1:
        printf("you can not drive");
        break;

    case 50:
        printf("you can not drive");
        break;
    
    default:
        printf("you can drive");
        break;
    }
    
    return 0;
}
