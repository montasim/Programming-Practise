#include <stdio.h>
int main()
{
    int num=1, input;
    scanf("%d", &input);
    printf("how many times you want the loop to run?\n");

    for (num; num <= input; num++)
    {
        printf("%d\n", num);
    }
    
    
    return 0;
}