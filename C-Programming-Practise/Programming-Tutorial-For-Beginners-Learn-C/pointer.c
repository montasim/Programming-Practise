#include <stdio.h>
int main()
{   
    int a=100;
    int* b=NULL;
    if(!b)
    {
        printf("pointer is null\n");
    }
    printf("%d\n", a);

    b=&a;
    *b=999;

    printf("%d", a);
    return 0;
}