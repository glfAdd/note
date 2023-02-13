package base;

/*
可变参数:
在方法声明中，在指定参数类型后加一个省略号(...)
一个方法中只能指定一个可变参数，它必须是方法的最后一个参数。任何普通的参数必须在它之前声明。

finalize()
Java 允许定义这样的方法，它在对象被垃圾收集器析构(回收)之前调用，这个方法叫做 finalize( )，它用来清除回收对象



*/
public class LearnFunc {
    public static void main(String[] args) {
        testFunc("aaa", 1.1, 1.2, 1.3, 22.1);
    }

    public static void testFunc(String a, double... number) {
        System.out.println(a);
        for (double i : number) {
            System.out.println(i);
        }
    }
}