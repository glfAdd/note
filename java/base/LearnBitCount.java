package base;
/*
位运算:
    超出范围的位删除, 新增的位补0
    << 左移, 左边除了符号位超出的部分删除, 右边空缺用0补
    >> 右移, 正数最高位用0补, 负数最高位用1补
    <<< 无符号左移,
    >>> 无符号右移, 无论负数还是正数最高位用0补
        00000011    3       3       3*2^0
       000000110    3<<1    6       3*2^1
      0000001100    3<<2    12      3*2^2
*/

public class LearnBitCount {
    public static void main(String[] args) {
        System.out.println(3 << 1);
        System.out.println(3 << 2);
        System.out.println(3 << 3);

        System.out.println("***************** 三元运算符");
        int a = 10, b = 30;
        int c = (a > b) ? a : b;
        System.out.println(c);
    }
}