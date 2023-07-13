import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int[] arr={2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9};
        int res = 0;
        String tmp=sc.nextLine();
        for(int i=0;i<tmp.length();i++){
            res+=arr[tmp.charAt(i)-'A']+1;
        }
        System.out.println(res);
    }
}