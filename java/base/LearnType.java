package base;
/*
局部变量:
    1. 访问修饰符不能用于局部变量；
    2. 局部变量是在栈上分配的。
    3. 局部变量没有默认值，所以局部变量被声明后，必须经过初始化，才可以使用。


实例变量
    1. 实例变量可以声明在使用前或者使用后；
    2. 访问修饰符可以修饰实例变量；
    3. 实例变量具有默认值。数值型变量的默认值是0，布尔型变量的默认值是false，引用类型变量的默认值是null
    4. 实例变量可以直接通过变量名访问。但在静态方法以及其他类中，就应该使用完全限定名：ObejectReference.VariableName。


类变量/静态变量
    类变量也称为静态变量，在类中以 static 关键字声明，但必须在方法之外。
    静态变量是指声明为 public/private，final 和 static 类型的变量。静态变量初始化后不可改变。
    静态变量储存在静态存储区。经常被声明为常量，很少单独使用 static 声明变量。
    静态变量在第一次被访问时创建，在程序结束时销毁。
    与实例变量具有相似的可见性。但为了对类的使用者可见，大多数静态变量声明为 public 类型
    数值型变量默认值是 0，布尔型默认值是 false，引用类型默认值是 null。静态变量还可以在静态语句块中初始化。
    静态变量可以通过：ClassName.VariableName的方式访问。
    类变量被声明为 public static final 类型时，类变量名称一般建议使用大写字母。如果静态变量不是 public 和 final 类型，其命名方式与实例变量以及局部变量的命名方式一致。


访问控制
    default: 默认, 在同一包内可见，不使用任何修饰符. 类、接口、变量、方法
    private: 在同一类内可见。使用对象：变量、方法。 注意：不能修饰类（外部类）
    public : 对所有类可见。使用对象：类、接口、变量、方法
    TODO protected 详细使用 https://www.runoob.com/w3cnote/java-protected-keyword-detailed-explanation.html
    protected : 对同一包内的类和所有子类可见。使用对象：变量、方法。 注意：不能修饰外部类, 可以修饰内部类。
            子类与基类在同一包中：被声明为 protected 的变量、方法和构造器能被同一个包中的任何其他类访问；
            子类与基类不在同一包中：那么在子类中，子类实例可以访问其从基类继承而来的 protected 方法，而不能访问基类实例的protected方法。


访问控制和继承
    1. 父类中声明为 public 的方法在子类中也必须为 public。
    2. 父类中声明为 protected 的方法在子类中要么声明为 protected，要么声明为 public，不能声明为 private。
    3. 父类中声明为 private 的方法，不能够被继承。


非访问修饰符
    static 修饰符，用来修饰类方法和类变量。
    final 修饰符，用来修饰类、方法和变量，final 修饰的类不能够被继承，修饰的方法不能被继承类重新定义，修饰的变量为常量，是不可修改的。
    abstract 修饰符，用来创建抽象类和抽象方法。
    synchronized 和 volatile 修饰符，主要用于线程的编程。    



static
    静态变量：无论一个类实例化多少对象，它的静态变量只有一份拷贝。 静态变量也被称为类变量。局部变量不能被声明为 static 变量
    静态方法：独立于对象, 静态方法不能使用类的非静态变量。静态方法从参数列表得到数据，然后计算这些数据。 


final 变量：
    被 final 修饰的实例变量必须显式指定初始值, 变量一旦赋值后不能被重新赋值
    final 修饰符通常和 static 修饰符一起使用来创建类常量
    父类中的 final 方法可以被子类继承，但是不能被子类重写, 可以防止该方法的内容被修改。
    final 类不能被继承，没有类能够继承 final 类的任何特性


abstract
    1. 声明抽闲类或抽象方法
    2. 抽象类不能用来实例化对象
    3. 一个类不能同时被 abstract 和 final 修饰

    1. 抽象方法是一种没有任何实现的方法，该方法的的具体实现由子类提供。
    2. 抽象方法不能被声明成 final 和 static。
    3. 任何继承抽象类的子类必须实现父类的所有抽象方法，除非该子类也是抽象类。
    4. 如果一个类包含抽象方法，那么该类必须声明为抽象类。抽象类可以不包含抽象方法。 


synchronized
    声明的方法同一时间只能被一个线程访问


TODO 看看用法
transient
    序列化的对象包含被 transient 修饰的实例变量时，java 虚拟机(JVM)跳过该特定的变量。
    该修饰符包含在定义变量的语句中，用来预处理类和变量的数据类型。 


volatile
    修饰的成员变量在每次被线程访问时，都强制从共享内存中重新读取该成员变量的值。
    而且，当成员变量发生变化时，会强制线程将变化值回写到共享内存。
    这样在任何时刻，两个不同的线程总是看到某个成员变量的同一个值。
    一个 volatile 对象引用可能是 null。 
*/

// 抽象类
abstract class AbstractTest {
    private double num;

    public abstract void work();

}

// 继承抽象类
class SubAbstractTest extends AbstractTest {
    public volatile boolean status = true;

    // 实现抽象方法
    public void work() {
        while (status) {
            System.out.println("func work");
        }

    }

    public void stop() {
        // 可以停止 work 中的循环
        status = false;
    }

    public synchronized void eat() {
    }

}

final class FinalTest {

}

public class LearnType {
    // 实例变量
    String address = "Lucy";
    static String name = "Tom";
    public int age;
    private int num;
    // TODO 静态变量初始化后不可改变, 实验测试?
    public static final String DEPARTMENT = "开发人员";

    public final void eat() {
        System.out.println("func eat");
    }

    public static void main(String[] args) {
        System.out.println("***************** 变量声明方式");
        // 局部变量
        int a, b, c;
        a = 11;
        int d = 1, e = 2, f = 3;

    }
}
