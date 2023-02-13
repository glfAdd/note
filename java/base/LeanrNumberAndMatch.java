package base;

/*
包装类 	        基本数据类型
Boolean 	    boolean
Byte 	        byte
Short 	        short
Integer 	    int
Long 	        long
Character 	    char
Float 	        float
Double 	        double

装箱: 内置数据类型被当作对象使用时
拆箱: 对象被当做内置类型使用时
Number 类属于 java.lang 包
*/
public class LeanrNumberAndMatch {
    public static void main(String[] args) {
        // x 被赋为整型值时，由于x是一个对象，所以编译器要对x进行装箱
        Integer a = 1;
        // 为了使x能进行加运算，所以要对x进行拆箱。 
        a = a + 3;
        System.out.println(a);
    }
}
