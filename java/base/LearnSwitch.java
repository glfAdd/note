/*
1. case 后面的常量和表达式进行匹配, 如果匹配成功则进入执行语句
2. 会一直向下执行知道遇到break或执行完
3. case和default的位置没有关系, 先执行case后再执行case
*/
public class LearnSwitch {
    public static void main(String[] args) {
        int a = 20;
        switch (a) {
            case 1:
            case 20:
                System.out.println(1);
//                break;
            case 2:
                System.out.println(2);
//                break;
            case 3:
                System.out.println(3);
                break;
            default:
                System.out.println("other");
                break;
        }
    }
}