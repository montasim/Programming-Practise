// finding the sum of the first 1011 natural numbers
#include <iostream>
using namespace std;

int findSum();

int main(){

    findSum();

    return 0;
}

int findSum() {
	int sum = 0;
	for (int v = 1; v <= 100000000000; v++) {
		sum += v;
	}
	return sum;
}
