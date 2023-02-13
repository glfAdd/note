package base;
/*
char 的包装类 Character

isLetter()          是否是一个字母
isDigit()           是否是一个数字字符
isWhitespace()      是否是一个空白字符
isUpperCase()       是否是大写字母
isLowerCase()       是否是小写字母
toUpperCase()       指定字母的大写形式
toLowerCase()       指定字母的小写形式 
toString()          返回字符的字符串形式，字符串的长度仅为1

*/

public class LearnCharacter {
    public static void main(String[] args){
        // 'c' 原始字符装箱到 Character 对象 a 中
        Character a = new Character('c');

        System.out.println(a);

    }
    
}
