package base;

public class LearnFor {
    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            System.out.println(i);
        }

        // 可以用于数组的循环
        int[] a = { 1, 2, 3, 4 };
        for (int i : a) {
            System.out.println(i);
        }
    }
}