#include <iostream>
using namespace std;

/*
默认第一个值为 0, 第一个值为 1, 第二个值为 2
可以指定值, 这里green 为 5, 后面的 blue 比 green 加 1

 */

enum color
{
    red,
    green = 5,
    blue
} a;
int main()
{

    a = red;
    cout << a;
    a = green;
    cout << a;
    a = blue;
    cout << a;
    return 0;
}
