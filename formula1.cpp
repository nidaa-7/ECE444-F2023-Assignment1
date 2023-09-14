#include <iostream>

int main(){
    
    int answer;

    std::cout<<"How many WDC should Lewis Hamilton have?"<<std::endl;
    std::cin>>answer;

    if(answer >= 8){
        std::cout<<"Cry about it."<<std::endl;
    }
    else if(answer == 7){
        std::cout<<"Fair!"<<std::endl;
    }
    else{
        std::cout<<"LOL"<<std::endl;
    }

    return 0;
}