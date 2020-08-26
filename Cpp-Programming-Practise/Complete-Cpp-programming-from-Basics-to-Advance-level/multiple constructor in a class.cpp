#include <iostream>
#include <string>
using namespace std;

class Car{
private:
    string name;
    string color;
    float price;
    int numberOfDoor;

public:
    Car(){
    name = "My Car";
    color = "Black";
    price = 1000.00;
    numberOfDoor = 2;
    }

    Car(string carName, string carColor, float carPrice, int carNumberOfDoor){
    name = carName;
    color = carColor;
    price = carPrice;
    numberOfDoor = carNumberOfDoor;
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
    car.setPrice(100);

    Car car2;
    car2.setPrice(60000);

    Car car3("car", "red", 3000, 4);
    return 0;
}
