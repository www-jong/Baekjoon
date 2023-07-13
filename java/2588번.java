import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);


        int first = sc.nextInt();
        String second = sc.next();
        char[] li = second.toCharArray();
        System.out.println(first*(int)(li[2]-'0'));
        System.out.println(first*(int)(li[1]-'0'));
        System.out.println(first*(int)(li[0]-'0'));
        System.out.println(first*Integer.parseInt(second));       
    }
}