#include <iostream>

int main(){
    std::cout<<"Hello World";  
    int a;
    std::cout<<"\nEnter Your Number :\n";
    std::cin >> a;
    std::cout<<"Enter a number :"<<a<<std::endl;
    for(int i=0;i<=a;i++){
        for(int j=0;j<=a;j++){
            std::cout<<j+1<<" ";
        }
        std::cout<<"\n";
    }
    for(int i=0;i<=a;i++){
        for(int j=0;j<=i;j++){
            std::cout<<"* ";
        }
        std::cout<<"\n";
    }
}