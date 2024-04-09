#include<iostream>
using namespace std;
class student{
    private:
    int id;
    char name[20];
    public:
    void getdata(){
        cout<<"enter id no: ";
        cin>>id;
        cout<<"enter name: ";
        cin>>name;
    }
    void show(){
        cout<<"id"<<id;
        cout<<"name"<<name;
    }
};

class stumarks:public student{
    int marks[3];
    public:
    void getmarks(){
        cout<<"enter 3 subject marks:";
        for(int i=0;i<3;i++){
            cin>>marks[i];
        }
    }

void showmarks(){
    cout<<"    3 subject marks";
    for(int i=0;i<3;i++){
        cout<<marks[i];

    }
}
};
int main(){
    stumarks s;
    s.getdata();
    s.getmarks();
    s.show();
    s.showmarks();
    return 0;
}