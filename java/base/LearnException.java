package base;

import java.io.*;

/*
异常和错误区别


继承关系
Throwable
    Exception
        IOException
        RuntimeException
    Error


自定义异常
    所有异常都必须是 Throwable 的子类。
    如果希望写一个检查性异常类，则需要继承 Exception 类。
    如果你想写一个运行时异常类，那么需要继承 RuntimeException 类。
*/

class MyException extends Exception {

}

public class LearnException {
    public static void main(String[] args) {
        try {
            System.out.println(1);
        } catch (ArrayIndexOutOfBoundsException a) {
            System.out.println(a);
//        } catch (IOException b) {
//            System.out.println(b);
        } finally {
            System.out.println("finally");
        }
//        手动抛出异常
        throw new ArrayIndexOutOfBoundsException();


    }
}
