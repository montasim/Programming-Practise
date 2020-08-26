#include <stdio.h>
int main()
{
    int num=1, input;
    scanf("%d", &input);
    printf("how many times you want the loop to run?\n");

    do
    {
        printf("%d\n", num);
        num++;
    } while (num <= input);
    
    
    return 0;
}