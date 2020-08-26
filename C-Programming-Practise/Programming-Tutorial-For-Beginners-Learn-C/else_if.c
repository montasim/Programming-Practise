#include <stdio.h>
int main()
{
    int age;
    printf("enter your age: \n");
    scanf("%d", &age);

    if(age<18)
    {
        printf("you can not drive");
    }
    else if(age>50)
    {
        printf("you can not drive");
    }
    else
    {
        printf("you can drive");
    }
    
    return 0;
}
