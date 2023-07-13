import java.io.IOException;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String[] arr=sc.nextLine().split(" ");
        String[] re_arr={"",""};
        for(int i=0;i<2;i++){
            for(int j=2;j>=0;j--){
                re_arr[i]+=String.valueOf(arr[i].charAt(j));
            }
        }
        if(Integer.parseInt(re_arr[0])>Integer.parseInt(re_arr[1])){
            System.out.println(re_arr[0]);
        }else{
            System.out.println(re_arr[1]);
        }
    }
}