#include <stdio.h>
int main()
{
    int a, float b=2.3;
    scanf("%d", &a);    //  & shows the address of variable where the input should go
    printf("%f", (float) a);    //  int to float
    printf("%d", (int) b);  //  float to int
    return 0;
}
