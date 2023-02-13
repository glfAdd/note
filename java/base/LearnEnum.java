package base;

/*
枚举:
    枚举可以有变量、方法和构造函数
    构造函数只能使用 private
    枚举可以包含具体方法和抽象方法. 如果枚举类具有抽象方法，则枚举类的每个实例都必须实现它


常用方法:
    values() 返回枚举类中所有的值。
    ordinal()方法可以找到每个枚举常量的索引，就像数组索引一样。
    valueOf()方法返回指定字符串值的枚举常量。

*/

// 类外部定义枚举
enum ColorOne {
    RED, BLACK, GREEN;

    // 有几个枚举常量就被调用几次
    private ColorOne() {
        System.out.println("init color one");
    }

    public void colorInfo() {
        System.out.println("color info");
    }
}

enum ColorThree {
    // 实现抽象方法
    PINK {
        public String getColor() {
            return "pink";
        }
    },
    BLACK {
        public String getColor() {
            return "black";
        }
    };

    // 定义抽象方法, 每个枚举常量必须实现这个枚举方法
    public abstract String getColor();

}

public class LearnEnum {
    // 类内部定义枚举
    enum ColorTwo {
        YELLOW, BLUE;
    }

    public static void main(String[] args) {
        ColorOne one = ColorOne.RED;
        System.out.println(one);
        one.colorInfo();

        ColorTwo two = ColorTwo.YELLOW;
        System.out.println(two);

        ColorThree three = ColorThree.PINK;
        System.out.println(three.getColor());


        for (ColorOne a : ColorOne.values()) {
            System.out.println(a);
        }

        switch (two) {
            case YELLOW:
                System.out.println("red");
                break;
            case BLUE:
                System.out.println("blue");
                break;
        }
    }


}
