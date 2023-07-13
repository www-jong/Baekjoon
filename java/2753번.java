import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int ans = sc.nextInt();
        if(ans%4==0 && (ans%100!=0 || ans%400==0 )){
            System.out.println("1");
        }else{
            System.out.println("0");
        }
    }
}