#include <stdio.h>
int main()
{
    const int pi=3.1416;
    printf("PI: %d", pi);
    pi=100; //  assignment of read-only variable 'pi'
    printf("PI: %d", pi);
    return 0;
}
