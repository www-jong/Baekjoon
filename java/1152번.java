import java.io.IOException;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String S = sc.nextLine();
        S=S.trim();
        if(S.length()>=1){
        String[] arr=S.split(" ");
        System.out.println(arr.length);
        }else{
            System.out.println(0);
        }
    }
}