package base;

/*
继承特性
    不支持多继承
    子类拥有父类非 private 的属性、方法。


关键字
    super：我们可以通过super关键字来实现对父类成员的访问，用来引用当前对象的父类。
    this： 指向自己的引用
    final: 定义的类不能被继承, 定义的方法不能重写, 定义的变量不能修改


构造器（构造方法或者构造函数）
    子类不继承父类的构造器, 它只是调用（隐式或显式）
    如果父类的构造器带有参数，则必须在子类的构造器中显式地通过 super 关键字调用父类的构造器并配以适当的参数列表。
    如果父类构造器没有参数，则在子类的构造器中不需要使用 super 关键字调用父类构造器，系统会自动调用父类的无参构造器


重写 Overriding
    1. 参数列表与被重写方法的参数列表必须完全相同
    2. 返回类型与被重写方法的返回类型可以不相同，但是必须是父类返回值的派生类
    3. 访问权限不能比父类中被重写的方法的访问权限更低。例如：如果父类的一个方法被声明为 public，那么在子类中重写该方法就不能声明为 protected。
    4. 声明为 final 的方法不能被重写
    5. 声明为 static 的方法不能被重写，但是能够被再次声明。
    6. 子类和父类在同一个包中，那么子类可以重写父类所有方法，除了声明为 private 和 final 的方法。
    7. 子类和父类不在同一个包中，那么子类只能够重写父类的声明为 public 和 protected 的非 final 方法。
    8. 重写方法不能抛出新的检查异常或者比被重写方法申明更加宽泛的异常。例如： 父类的一个方法申明了一个检查异常 IOException，但是在重写这个方法的时候不能抛出 Exception 异常，因为 Exception 是 IOException 的父类，只能抛出 IOException 的子类异常
    9. 构造方法不能被重写


重载 overloading
    被重载的方法必须改变参数列表(参数个数或类型不一样)
    被重载的方法可以改变返回类型；
    被重载的方法可以改变访问修饰符；
    被重载的方法可以声明新的或更广的检查异常；
    方法能够在同一个类中或者在一个子类中被重载。
    无法以返回值类型作为重载函数的区分标准。



*/


class Animal {
    public int age = 10;

    // 无参数构造函数
    Animal() {
        System.out.println("animal 无参数");
    }

    // 有参数构造函数
    Animal(int n) {
        System.out.println("animal 有参数");
    }

    public void run() {
        System.out.println("run ------");
    }

    final void sleep() {
        System.out.println("sleep ----");
    }
}

class Cat extends Animal {
    // 自动调用父类无参数构造函数
    Cat(int a) {
        System.out.println("cat 有参数构造函数");
    }

    // 手动调用父类有参数构造函数
    Cat() {
        super(100);
        System.out.println("cat 无参数构造函数");
    }

    public void run(int age) {
        // 变量名和类变量名冲突
        this.age = age;
        System.out.println(this.age);
    }

    public void eat() {
        System.out.println("eat ------");
        // 调用自己的run方法
        this.run(10086);
        // 调用父类的 run
        super.run();
        sleep();
    }
}


public class LearnExtends {
    public static void main(String[] args) {
        Cat c = new Cat();
        c.eat();
        c.run();
        System.out.println(c.age);

        Cat c2=new Cat(55);
    }
}
