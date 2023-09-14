#include <iostream>
#include <string>
#include <algorithm>

int main(){
    std::string answer;

    std::cout<<"What is the best soccer team in the world?"<<std::endl;
    std::getline(std::cin, answer);

    std::transform(answer.begin(), answer.end(), answer.begin(), ::tolower);

    if(answer == "real madrid"){
        std::cout<<"That's right!"<<std::endl;
    }
    else{
        std::cout<<"Game over, try again..."<<std::endl;
    }

    return 0;
}