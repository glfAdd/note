#include <iostream>
using namespace std;

/*
全局变量

定义局部变量时, 必须手动初始化
定义全局变量时，系统会自动初始化
    int     0
    char    '\0'
    float   0
    double  0
    pointer NULL

*/
int age = 10;

int main()
{
    int a, b;
    a = 1;
    b = 2;
    int c = a + b;
    cout << c << endl;

    cout << age << endl;
    // 局部变量和全局变量的名称可以相同, 但局部变量会覆盖全局变量
    int age = 20;
    cout << age << endl;
}