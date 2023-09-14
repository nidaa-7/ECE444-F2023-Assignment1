// Simple program that prints your age in 2023 based on the year you were born

#include <iostream>
#include <math.h>
#define year 2023

int main(){
    int born, age;

    std::cout<<"Enter the year you were born in: ";
    std::cin>>born;

    age = year - born;

    std::cout<<"You are "<< age << " years old" << std::endl;

    return 0;
}