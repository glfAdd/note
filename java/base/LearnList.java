package base;

/*
Java 语言中提供的数组是用来存储固定大小的同类型元素。


* */

public class LearnList {
    public static void main(String[] args) {
        double[] a;
        double[] b = new double[10];
        double[] c = {1, 2, 3, 4, 5, 6};
        c[1] = 44.2;
        for (double item : c) {
            System.out.println(item);
        }

        double[][] d = new double[5][5];
        d[1][2] = 12.1;
    }
}
