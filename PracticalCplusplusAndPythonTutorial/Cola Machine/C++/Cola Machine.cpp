// Cola Machine.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

using namespace std;

int main()
{
	cout << "Hello and Welcome to this non-existent Vending Machine!" << endl;

	this_thread::sleep_for(2s);

	cout << "Choose your Beverage!\n" << endl;
	cout << "1. Water" << endl;
	cout << "2. Sparking Water" << endl;
	cout << "3. Lemon Sparkling Water" << endl;
	cout << "4. Orange Sparkling Water" << endl;
	cout << "5. Milk" << endl;

	int choice = 0;

	cin >> choice;

	switch (choice) {
	case 1:
			cout << "You chose Water!" << endl;
			system("PAUSE");
			break;
	case 2:
		cout << "You chose Sparking Water" << endl;
		system("PAUSE");
		break;

	case 3:
		cout << "You chose Lemon Sparking Water" << endl;
		system("PAUSE");
		break;

	case 4:
		cout << "You chose Orange Sparking Water" << endl;
		system("PAUSE");
		break;

	case 5:
		cout << "You chose Milk" << endl;
		system("PAUSE");
		break;

	default:
		cout << "Hey, that was not vaild!" << endl;
		this_thread::sleep_for(1s);
		cout << "Here is a refund!" << endl;
		system("PAUSE");

	}

    return 0;
}

