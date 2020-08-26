#include <iostream>
#include <string.h>

using namespace std;

class Shape{
public:
    int height;
    int weidht;

    void area(){
        cout << "base class" << endl;
    }
};

class Squre: public Shape{
public:
    int side;

    void area(int x){
        side = x;
        cout << "Squre area is "<< side * side << endl;
    }
};
class Triangle: public Shape{
public:
    int side;

    void area(int x){
        side = x;
        cout << "Triangle area is "<< (side * side) / 2 << endl;
    }
};

class Rectangle: public Shape{
public:
    int side;

    void area(int x){
        side = x;
        cout << "Rectangle area is "<< side * side << endl;
    }
};

int main()
{
    Squre squre;
    Triangle triangle;
    Rectangle rectangle;

    squre.area(2);
    triangle.area(2);
    rectangle.area(2);

    return 0;
}


