package base;

/*
package
    Java 提供了包机制，用于区别类名的命名空间
    同一个包中的类名字不能相同
    包声明应该在源文件的第一行，每个源文件只能有一个包声明
    如果一个源文件中没有使用包声明，那么其中的类，函数，枚举，注释等将被放在一个无名的包（unnamed package）中


包命名规则:
    通常，一个公司使用它互联网域名的颠倒形式来作为它的包名. 例如：互联网域名是 runoob.com，所有的包名都以 com.runoob 开头。包名中的每一个部分对应一个子目录
    例如：有一个 com.runoob.test 的包，这个包包含一个叫做 Runoob.java 的源文件，那么相应的，应该有如下面的一连串子目录：
    ....\com\runoob\test\Runoob.java
    编译的时候，编译器为包中定义的每个类、接口等类型各创建一个不同的输出文件，输出文件的名字就是这个类型的名字，并加上 .class 作为扩展后缀


import
如果在一个包中，一个类想要使用本包中的另一个类，那么该包名可以省略


java 文件的编译
类目录的绝对路径叫做 class path。设置在系统变量 CLASSPATH 中

编译
javac -d . LearnPackage.java

根据package的路径, 在当前目录下生成文件夹, 里面是和类名相同的class文件

*/
public class LearnPackage {
    public static void main(String[] args) {
        System.out.println("run");
    }
}
