package base;
/*
多态: 同一个接口，使用不同的实例而执行不同操作
多态存在的三个必要条件: 继承, 重写, 父类引用指向子类对象
使用多态方式调用方法时，首先检查父类中是否有该方法，如果没有，则编译错误；如果有，再去调用子类的同名方法。


虚函数



*/

class Person {
    public void run() {
        System.out.println("person run");
    }
}

class Tom extends Person {
    public void run() {
        System.out.println("tom run");
    }
}

class Lucy extends Person {
    public void run() {
        System.out.println("lucy run");
    }
}

public class LearnDuoTai {
    public static void main(String[] args) {
        Tom t = new Tom();
        Lucy l = new Lucy();
        test(t);
        test(l);
    }

    public static void test(Person p) {
        p.run();
    }
}
