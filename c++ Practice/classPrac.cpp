//
// Created by Shahroz Imtiaz on 2019-08-29.
//
#include <iostream>
using namespace std;

class Person {
    private:
        int id;
    public:
        Person(int id){
            this->id = id;
        }
        int getId(){
            return this->id;
        }
};

int main() {
    Person* p1 = new Person(7);
    Person* p2 = new Person(14);
    cout<<p2->getId()<<endl;
}