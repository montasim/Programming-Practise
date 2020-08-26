#include <iostream>
#include <string>
using namespace std;

class Car{
public:
    string name;
    string color;
    float price;
    int numberOfDoor;

    Car(){
    name = "My Car";
    color = "Black";
    price = 1000.00;
    numberOfDoor = 2;
    }

    setName(string newName){
    name = newName;
    }

    setColor(string newColor){
    color = newColor;
    }

    setPrice(float newPrice){
    if(newPrice > 0)
        price = newPrice;
    else
        cout << "Invalid Price" << endl;
    }

    setNumberOfDoor(int newNumberOfDoor){
    numberOfDoor = newNumberOfDoor;
    }
};

int main(){
    Car car;
    cout << car.name << endl;
    cout << car.color << endl;
    cout << car.price << endl;
    cout << car.numberOfDoor << endl << endl;

    car.name = "New Car";
    cout << car.name << endl << endl;

    //car.price = -900;

    car.setPrice(100);
    cout << car.price << endl << endl;
    cout << endl;

    Car car2;
    cout << car2.name << endl;
    cout << car2.color << endl;
    cout << car2.price << endl;
    cout << car2.numberOfDoor << endl << endl;

    car2.setPrice(-1000);
    cout << car2.price << endl;
    return 0;
}
