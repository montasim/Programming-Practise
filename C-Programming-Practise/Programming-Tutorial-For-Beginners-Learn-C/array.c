#include <stdio.h>
int main()
{   
    int array[100], input;

    printf("enter size of array: ");
    scanf("%d", &input);

    for (int i = 0; i < input; i++)
    {
        printf("Enter values for index[%d] = ", i);
        scanf("%d", &array[i]);
    }

    for (int i = 0; i < input; i++)
    {
        printf("value for index[%d] = %d\n", i, array[i]);
    }
   
}
