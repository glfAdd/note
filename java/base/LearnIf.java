public class LearnIf {
    public static void main(String[] args) {
        int a = 1;
        if (a == 10) {
            System.out.println(10);
        } else if (a == 11) {
            System.out.println(11);
        } else {
            System.out.println("other");
        }

//        如果if语句中只有一条执行语句可以省略{}, 最好不省略
        if (a == 31)
            System.out.println("31");

    }
}