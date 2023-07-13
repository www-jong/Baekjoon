import java.io.IOException;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        String tmp=sc.nextLine();
        int res= 0 ;
        for(int i=0;i<tmp.length();i++){
            res+=tmp.charAt(i)-'0';
        }
        System.out.println(res);
    }
}