package base;

/*

接口特点
    接口不是类
    实现接口的类，必须实现接口内所描述的所有方法，否则就必须声明为抽象类
    接口不能实例化对象
    接口没有构造方法
    接口中所有的方法必须是抽象方法
    接口支持多继承
    接口中方法会被隐式的指定为 public abstract,
    接口中方法只能是 public abstract，其他修饰符都会报错, 可以隐式指定
    接口中变量只能是 public static final, 其他会报错, 可以隐式指定
    一个类只能继承一个抽象类，而一个类却可以实现多个接口



*/
interface Car {
    public void run();

    public void open();
}


public class LearnInterface implements Car {
    public void run() {
        System.out.println("run");
    }

    public void open() {
        System.out.println("open");
    }

    public static void main(String[] args) {
        Car c = new LearnInterface();
        c.run();
        c.open();
    }
}
