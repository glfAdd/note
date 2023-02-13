import java.util.Scanner;

public class LearnScanner {
    public static void main(String[] args) {
        Scanner a = new Scanner(System.in);
        System.out.println("请输入1: ");
        int num = a.nextInt();
        System.out.println(num);

        System.out.println("请输入2: ");
        double num2 = a.nextDouble();
        System.out.println(num2);

    }
}