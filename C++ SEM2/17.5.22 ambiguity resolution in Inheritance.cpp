#include <iostream>  
using namespace std;  
class A  
{  
    public:  
    void display()  
    {  
        std::cout << "Class A" << endl;  
    }  
};  
class B  
{  
    public:  
    void display()  
    {  
        std::cout << "Class B" << endl;  
    }  
};  
/*
class C : public A, public B  
{  
    void view()  
    {  
        display();  
    }  
};  */

class C : public A, public B  
{  
    void view()  
    {  
        A :: display();         // Calling the display() function of class A 
        B :: display();         // Calling the display() function of class B
  
    }  
}; 

int main()  
{  
    C c;  
    c.A::display();  
    c.B::display(); 
    return 0;  
} 

