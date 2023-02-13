package base;

/*

抽象类
    抽象类除了不能实例化对象之外，类的其它功能依然存在，成员变量、成员方法和构造方法的访问方式和普通类一样。
    抽象类必须被继承，才能被使用


抽象方法
    抽象方法只声明, 没有具体的实现
    如果一个类包含抽象方法，那么该类必须是抽象类
    任何子类必须重写父类的抽象方法，或者声明自身为抽象类
    抽象类中的抽象方法只是声明，不包含方法体
    构造方法，类方法（用 static 修饰的方法）不能声明为抽象方法



*/
abstract class TestAbstract {
    String name = "Tom";

    public void run() {
        System.out.println("run ----- ");
    }

    public abstract double eat();

}

class TestAbstract2 extends TestAbstract {
    public double eat() {
        System.out.println(name);
        return 110.0;
    }
}

public class LearnAbstract {
    public static void main(String[] args) {
        TestAbstract a = new TestAbstract2();
        a.run();
        a.eat();
    }
}
