package base;
/*
构造方法:
    每个类都有构造方法。如果没有显式地为类定义构造方法，Java 编译器将会为该类提供一个默认构造方法。
    在创建一个对象的时候，至少要调用一个构造方法。构造方法的名称必须与类同名，一个类可以有多个构造方法。


内部类: 一个类中嵌套另一个类
    静态内部类
    非静态内部类


匿名内部类:
    1. 必须继承一个父类或实现一个接口, 切只能是其中一个, 继承父类重写的方法父类必须存在
    2. 没有 class 关键字, 用 new 声明
    3. 匿名内部类中是不能定义构造函数
    4. 匿名内部类中不能存在任何的静态成员变量和静态方法
    5. 匿名内部类为局部内部类，所以局部内部类的所有限制同样对匿名内部类生效
    6. 匿名内部类不能是抽象的，它必须要实现继承的类或者实现的接口的所有抽象方法
    

1. 一个源文件中只能有一个 public 类, 可以有多个非 public 类 
2. 源文件的名称应该和 public 类的类名保持一致。例如：源文件中 public 类的类名是 Employee，那么源文件应该命名为Employee.java。
3. 如果一个类定义在某个包中，那么 package 语句应该在源文件的首行。
5. 如果源文件包含 import 语句，那么应该放在 package 语句和类定义之间。如果没有 package 语句，那么 import 语句应该在源文件中最前面。
6. import 语句和 package 语句对源文件中定义的所有类都有效。在同一源文件中，不能给不同的类不同的包声明。

*/

class OutClass {
    int x = 100;

    // 私有内部类, 外部类外面的类无法访问
    private class InClassPrivate {
        int z = 300;
    }

    class InClass {
        int y = 200;
        InClassPrivate inPrivate = new InClassPrivate();
    }

    // 静态内部类无法访问外部类成员变量
    class InClassStatic {
        int z = 40;
    }

    public void run(){
        System.out.println("run 方法");
    }

}

public class LearnClass {
    String name;
    // 类方法必须用 static 声明
    static int age;

    // 构造方法
    public LearnClass() {
    }

    public LearnClass(String name) {
        System.out.println(name);
    }

    public void setAge(int num) {
        age = num;
    }

    public int getAge() {
        return age;
    }

    void eat() {
        System.out.println("-----" + age);

    }

    public static void main(String[] args) {
        // 使用 new 创建对象
        LearnClass l = new LearnClass("小明");
        l.setAge(12);
        l.eat();
        System.out.println(l.getAge());

        // 使用内部类
        OutClass out = new OutClass();
        OutClass.InClass in = out.new InClass();
        System.out.println(out.x + in.y);

        // 是有内部类, 这里不可使用
        // OutClass.InClassPrivate inPrivate = out.new InClassPrivate();

        // 静态内部类
        OutClass.InClassStatic inStatic = out.new InClassStatic();
        System.out.println(inStatic.z);

        // 匿名类
        OutClass niMingClass = new OutClass(){
            public void run(){
                System.out.println("匿名类调用 run 方法");
            }
        };
        niMingClass.run();


    }

}
