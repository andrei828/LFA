#include <time.h>
#include <stdio.h>

void delay(int number_of_seconds) 
{ 
    // Converting time into milli_seconds 
    int milli_seconds = CLOCKS_PER_SEC * number_of_seconds; 
  
    // Stroing start time 
    clock_t start_time = clock(); 
  
    // looping till required time is not acheived 
    while (clock() < start_time + milli_seconds); 
}

void printMenu1() {
	printf("\033[2J\033[0;0H");

	printf("\n\033[37;1mUser 1 ");
	printf("\033[44;1m  P1  ");
	printf("\033[45;1m P2 ");
	printf("\033[42;1m  P3  ");
	printf("\033[m\n");

	printf("\033[37;1mUser 2 ");
	printf("\033[43;1m  P1  ");
	printf("\033[46;1m P2 ");
	printf("\033[41;1m  P3  ");
	printf("\033[42;1m   P4   ");
	printf("\033[45;1m  P5  ");
	printf("\033[m\n");

	printf("\n\033[37;1mProcessor ");

	// int x;
	// fscanf(stdin, "%d", &x);
	printf("\033[2K \033[0GHello\n");
}

void printMenu2() {
	printf("\033[2J\033[0;0H");

	printf("\n\033[37;1mUser 1 ");
	printf("\033[42;1m  P3  ");
	printf("\033[m\n");

	printf("\033[37;1mUser 2 ");
	printf("\033[43;1m  P1  ");
	printf("\033[46;1m P2 ");
	printf("\033[41;1m  P3  ");
	printf("\033[42;1m   P4   ");
	printf("\033[45;1m  P5  ");
	printf("\033[m\n");


	printf("\n\033[37;1mProcessor ");

	// int x;
	// fscanf(stdin, "%d", &x);
	printf("\033[2K \033[0GHello\n");
}

void printMenu3() {
	printf("\033[2J\033[0;0H");

	printf("\033[37;1mUser 1  ");
	printf("\033[42;1m  P3  ");
	printf("\033[43;1m  P1  ");
	printf("\033[46;1m P2 ");
	printf("\033[41;1m  P3  ");
	printf("\033[m\n");

	printf("\033[37;1mUser 2  ");
	printf("\033[42;1m   P4   ");
	printf("\033[45;1m  P5  ");
	printf("\033[m\n");
	printf(" ....\n");
	printf("\033[37;1mUser 8  ");
	printf("\033[42;1m  P3  ");
	printf("\033[43;1m  P1  ");
	printf("\033[46;1m P2 ");
	printf("\033[41;1m  P3  ");
	printf("\033[m\n");
	printf("\033[37;1mUser 9  ");
	printf("\033[43;1m  P1  ");
	printf("\033[46;1m P2 ");
	printf("\033[41;1m  P3  ");
	printf("\033[42;1m  P3  ");
	printf("\033[m\n");

	printf("\033[37;1mUser 10 ");
	printf("\033[42;1m   P4   ");
	printf("\033[45;1m  P5  ");
	printf("\033[m\n");


	printf("\n\033[37;1mProcessor ");

	// int x;
	// fscanf(stdin, "%d", &x);
	printf("\033[2K \033[0G\n");
}

int main() {

	printMenu3();
	// delay(2);
	// printMenu2();
	// delay(2);
	// printMenu3();
	// delay(2);
}