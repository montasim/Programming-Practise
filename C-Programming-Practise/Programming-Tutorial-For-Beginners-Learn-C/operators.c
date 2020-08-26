#include <stdio.h>
int main()
{
    int a=1, b=2, c=3;

    //  arithmatic operator
    printf("a+b+c= %d\n", a+b+c);
    printf("a-b-c= %d\n", a-b-c);
    printf("a*b*c= %d\n", a*b*c);
    printf("a/b/c= %d\n\n", a/b/c);

    //  relational operator
    printf("%d\n", a==b==c);
    printf("%d\n", a!=b!=c);
    printf("%d\n", a<b<c);
    printf("%d\n\n", a>b>c);

    //  logical operator
    printf("%d\n", a&&b&&c);
    printf("%d\n", a||b||c);
    printf("%d\n", !a);
    printf("%d\n", !b);
    printf("%d\n\n", !c);

    //  bitwise operator
    printf("%d\n", a&b&c);
    printf("%d\n", a|b|c);
    printf("%d\n", ~a);
    printf("%d\n", ~b);
    printf("%d\n", ~c);
    printf("%d\n", a<<b<<c);
    printf("%d\n\n", a>>b>>c);

    //  assignment operator
    int assignment=1;
    assignment +=1; 
    printf("%d\n", assignment);
    // printf("%d\n", +=2;
    // printf("%d\n", +=3);
    // printf("%d\n", -=1);
    // printf("%d\n", -=2);
    // printf("%d\n\n", -=3);

    // misc operators &, *, ?

    return 0;
}