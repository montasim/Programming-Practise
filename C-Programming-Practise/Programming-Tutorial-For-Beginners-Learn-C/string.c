#include <stdio.h>
#include <string.h>
int main()
{   
    char str1[10]="hello", str2[10]="world";

    printf("%s\n", str1);
    printf("%s\n", str2);

    /*strcat(str1, str2);
    printf("%s\n", str1);

    strcpy(str1, str2);
    printf("%s\n", str1);*/

    printf("%d\n", strcmp(str1, str2)); //  strcmp return 0 when str1==str2, -1 when str1<str2, +1 when str1>str2

    return 0;
}