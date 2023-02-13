package base;
/*
string 包装类 String
String 创建的字符串存储在公共池中，而 new 创建的字符串对象在堆上：


*/

public class LearnString {
    public static void main(String[] args) {
        String a = "字符串";
        String b = new String("拼接");
        System.out.println(a + b);

//      生成字符串
        char[] c = {'a', 'b', 'c', 'd'};
        String d = new String(c);
        System.out.println(d);
//      字符串长度
        System.out.println(d.length());


    }
}
